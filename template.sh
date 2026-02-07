
#!/usr/bin/env bash

set -o noclobber

usage() {
  echo "Usage: $0 <year: 4-digit> <day: 1-25>"
  exit 1
}

# ---- Argument parsing and validation ----
if [[ $# -ne 2 ]]; then
  usage
fi

year="$1"
day="$2"

if ! [[ "$year" =~ ^[0-9]{4}$ ]]; then
  echo "Error: year must be a 4-digit number." >&2
  exit 2
fi

if ! [[ "$day" =~ ^[0-9]+$ ]] || (( day < 1 || day > 25 )); then
  echo "Error: day must be an integer between 1 and 25." >&2
  exit 3
fi

# ---- Paths ----
base_dir="$HOME/aoc/$year/$day"
data_target="$HOME/aoc-data/$year/$day.txt"
data_target_rel="../../../aoc-data/$year/$day.txt"
data_source="$HOME/werffmrvd/Downloads/input.txt"
sample_file="$base_dir/ref.txt"


# ---- Safety: refuse if the directory already exists ----
if [[ -e "$base_dir" ]]; then
  echo "Error: target directory already exists: $base_dir" >&2
  echo "Refusing to overwrite. Choose a different day or remove the directory first." >&2
  exit 4
fi

echo "Creating $base_dir"
mkdir -p "$base_dir"

echo "Creating symlink $base_dir/input.txt --> $data_target_rel"
ln -sfn "$data_target_rel" "$base_dir/input.txt"

# ---- Python template ----
read -r -d '' py_template <<PYCODE
#!/usr/bin/env python3

total = 0
with open(0) as f:
    for line in f:
        line = line.strip()
        print(line)
    # grid = [list(line.strip()) for line in f]
    # nrows, ncols = len(grid), len(grid[0])

# for row in grid:
#     print(" ".join(row))

print(total)
PYCODE

# ---- Create both files and make them executable ----
for suffix in a b; do
  fpath="$base_dir/aoc-${year}-${day}${suffix}.py"
  echo "Creating $fpath"
  printf "%s\n" "$py_template" > "$fpath"
  chmod +x "$fpath"
done

# ---- Sample file ----
echo "Creating $sample_file"
touch $sample_file

if [[ -f "$data_source" ]]; then
  mv "$data_source" "$data_target"
  echo "Moved: $data_source --> $data_target"
else
  # echo "Data source not found in $data_source"
  echo "Execute: mv $data_source $data_target"
fi
