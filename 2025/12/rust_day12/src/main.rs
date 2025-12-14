use clap::Parser;
use std::collections::{HashMap, HashSet};
use std::fs::File;
use std::io::{BufRead, BufReader};

type Shape = Vec<Vec<char>>;

/// Command-line arguments
#[derive(Parser, Debug)]
#[command(author, version, about)]
struct Args {
    /// Input file
    #[arg(short = 'f', long = "file", default_value = "input.txt")]
    file: String,

    /// Show solution
    #[arg(long = "show-solution", default_value_t = false)]
    show_solution: bool,
}

#[derive(Clone, PartialEq, Eq, Hash)]
struct BitSet {
    bits: Vec<u64>,
}

impl BitSet {
    fn new(size: usize) -> Self {
        BitSet {
            bits: vec![0u64; size.div_ceil(64)]
        }
    }

    fn set(&mut self, idx: usize) {
        let word = idx / 64;
        let bit = idx % 64;
        self.bits[word] |= 1u64 << bit;
    }

    fn _is_set(&self, idx: usize) -> bool {
        let word = idx / 64;
        let bit = idx % 64;
        (self.bits[word] & (1u64 << bit)) != 0
    }

    fn intersects(&self, other: &BitSet) -> bool {
        for i in 0..self.bits.len() {
            if (self.bits[i] & other.bits[i]) != 0 {
                return true;
            }
        }
        false
    }

    fn union(&self, other: &BitSet) -> BitSet {
        let mut result = self.clone();
        for i in 0..result.bits.len() {
            result.bits[i] |= other.bits[i];
        }
        result
    }
}

fn rotate90(shape: &Shape) -> Shape {
    let h = shape.len();
    let w = shape[0].len();
    let mut result = vec![vec!['.'; h]; w];
    for r in 0..h {
        for c in 0..w {
            result[c][h - 1 - r] = shape[r][c];
        }
    }
    result
}

fn orientations(shape: &Shape) -> Vec<Shape> {
    let mut result = vec![shape.clone()];
    let mut current = shape.clone();
    for _ in 0..3 {
        current = rotate90(&current);
        result.push(current.clone());
    }
    result
}

fn shape_area(shape: &Shape) -> usize {
    shape
        .iter()
        .flat_map(|row| row.iter())
        .filter(|&&c| c == '#')
        .count()
}

fn shape_offsets(shape: &Shape) -> (Vec<(usize, usize)>, usize, usize) {
    let h = shape.len();
    let w = shape[0].len();
    let mut offs = Vec::new();
    for r in 0..h {
        for c in 0..w {
            if shape[r][c] == '#' {
                offs.push((r, c));
            }
        }
    }
    (offs, h, w)
}

fn render_board_labels(
    w: usize,
    h: usize,
    placements: &[(char, Vec<(usize, usize)>, usize, usize)],
) -> Vec<String> {
    let mut board = vec![vec!['.'; w]; h];
    for (label, offs, tx, ty) in placements {
        for (dy, dx) in offs {
            board[ty + dy][tx + dx] = *label;
        }
    }
    board
        .iter()
        .map(|row| {
            row.iter()
                .map(|&c| c.to_string())
                .collect::<Vec<_>>()
                .join(" ")
        })
        .collect()
}

#[derive(Clone)]
struct Placement {
    mask: BitSet,
    offs: Vec<(usize, usize)>,
    tx: usize,
    ty: usize,
}

fn precompute_placements(w: usize, h: usize, shapes: &[Shape]) -> Vec<Vec<Placement>> {
    let board_size = w * h;
    let mut placements_by_idx = Vec::new();

    for base in shapes {
        let mut plist = Vec::new();
        for o in orientations(base) {
            let (offs, rh, rw) = shape_offsets(&o);
            for ty in 0..=(h.saturating_sub(rh)) {
                for tx in 0..=(w.saturating_sub(rw)) {
                    let mut m = BitSet::new(board_size);
                    for (dy, dx) in &offs {
                        let idx = (ty + dy) * w + (tx + dx);
                        m.set(idx);
                    }
                    plist.push(Placement {
                        mask: m,
                        offs: offs.clone(),
                        tx,
                        ty,
                    });
                }
            }
        }

        // Deduplicate identical masks
        let mut seen = HashSet::new();
        let mut uniq = Vec::new();
        for p in plist {
            if seen.insert(p.mask.clone()) {
                uniq.push(p);
            }
        }
        placements_by_idx.push(uniq);
    }

    placements_by_idx
}

fn can_all_fit(
    w: usize,
    h: usize,
    present_counts: &[usize],
    shapes: &[Shape],
    show_solution: bool,
) -> (bool, Vec<String>) {
    let total_needed: usize = present_counts
        .iter()
        .enumerate()
        .map(|(i, &c)| shape_area(&shapes[i]) * c)
        .sum();

    if total_needed > w * h {
        return (false, Vec::new());
    }

    let placements_by_idx = precompute_placements(w, h, shapes);
    let areas: Vec<usize> = shapes.iter().map(shape_area).collect();

    let mut counts = present_counts.to_vec();
    let total_to_place: usize = counts.iter().sum();
    let mut memo = HashMap::new();
    let mut placement_stack = Vec::new();
    let board_size = w * h;

    fn backtrack(
        placed: usize,
        mask: &BitSet,
        total_to_place: usize,
        counts: &mut [usize],
        placements_by_idx: &[Vec<Placement>],
        areas: &[usize],
        memo: &mut HashMap<(BitSet, Vec<usize>), bool>,
        placement_stack: &mut Vec<(char, Vec<(usize, usize)>, usize, usize)>,
    ) -> bool {
        if placed == total_to_place {
            return true;
        }

        let key = (mask.clone(), counts.to_vec());
        if memo.contains_key(&key) {
            return false;
        }

        // Build feasible placements per remaining shape
        let mut candidates_per_shape = Vec::new();
        for i in 0..counts.len() {
            if counts[i] == 0 {
                continue;
            }
            let feasible: Vec<&Placement> = placements_by_idx[i]
                .iter()
                .filter(|p| !p.mask.intersects(mask))
                .collect();

            if feasible.is_empty() {
                memo.insert(key, false);
                return false;
            }
            candidates_per_shape.push((i, feasible));
        }

        // MRV: choose shape with fewest feasible placements; tie-break by larger area
        candidates_per_shape.sort_by_key(|(i, feasible)| (feasible.len(), -(areas[*i] as i32)));
        let (shape_idx, feasible_list) = &candidates_per_shape[0];

        let label = if placed < 26 {
            (b'A' + placed as u8) as char
        } else {
            '*'
        };

        for p in feasible_list.iter() {
            counts[*shape_idx] -= 1;
            placement_stack.push((label, p.offs.clone(), p.tx, p.ty));

            let new_mask = mask.union(&p.mask);
            if backtrack(
                placed + 1,
                &new_mask,
                total_to_place,
                counts,
                placements_by_idx,
                areas,
                memo,
                placement_stack,
            ) {
                return true;
            }

            placement_stack.pop();
            counts[*shape_idx] += 1;
        }

        memo.insert(key, false);
        false
    }

    let empty_mask = BitSet::new(board_size);
    let success = backtrack(
        0,
        &empty_mask,
        total_to_place,
        &mut counts,
        &placements_by_idx,
        &areas,
        &mut memo,
        &mut placement_stack,
    );

    if !success {
        return (false, Vec::new());
    }

    if show_solution {
        let board_lines = render_board_labels(w, h, &placement_stack);
        (true, board_lines)
    } else {
        (true, Vec::new())
    }
}

fn day12(filename: &str, show_solution: bool) -> std::io::Result<()> {
    let file = File::open(filename)?;
    let reader = BufReader::new(file);

    let mut shapes_dict: HashMap<usize, Shape> = HashMap::new();
    let mut presents = Vec::new();
    let mut current_idx: Option<usize> = None;

    for line in reader.lines() {
        let line = line?;
        let trimmed = line.trim();

        if trimmed.ends_with(':') && !trimmed.contains('x') {
            let idx = trimmed[..trimmed.len() - 1].parse::<usize>().unwrap();
            current_idx = Some(idx);
            shapes_dict.insert(idx, Vec::new());
        } else if trimmed.contains('.') || trimmed.contains('#') {
            if let Some(idx) = current_idx {
                shapes_dict
                    .get_mut(&idx)
                    .unwrap()
                    .push(trimmed.chars().collect());
            }
        } else if trimmed.contains(':') {
            let parts: Vec<&str> = trimmed.split(": ").collect();
            let dims: Vec<usize> = parts[0].split('x').map(|s| s.parse().unwrap()).collect();
            let counts: Vec<usize> = parts[1]
                .split_whitespace()
                .map(|s| s.parse().unwrap())
                .collect();
            presents.push((dims[0], dims[1], counts));
        }
    }

    let mut shapes = Vec::new();
    for i in 0..shapes_dict.len() {
        shapes.push(shapes_dict[&i].clone());
    }

    let mut total = 0;
    for (region_idx, (w, h, counts)) in presents.iter().enumerate() {
        let (ok, board_lines) = can_all_fit(*w, *h, counts, &shapes, show_solution);
        print!(
            "Region {}: {}x{} with counts {:?}: fits ",
            region_idx + 1,
            w,
            h,
            counts
        );

        if ok {
            println!("YES");
            total += 1;
            if show_solution {
                println!();
                for line in board_lines {
                    println!("{}", line);
                }
                println!();
            }
        } else {
            println!("NO");
        }
    }

    println!("\nTotal: {}", total);
    Ok(())
}

fn main() -> std::io::Result<()> {
    let args = Args::parse();
    day12(&args.file, args.show_solution)
}
