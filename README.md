# Advent of Code

[Advent of Code](https://adventofcode.com/) is an Advent calendar of small programming puzzles for a
variety of skill levels that can be solved in any programming language you like. I started in 2025 and I am working my way back. Python was used to solve most puzzles.

## Re-usable stuff

* Grid with S and E target in 2023:10
* Combining ranges in 2023:5b, improved in 2022:15
* Moving grid obstacles in 2022:24
* Generic dijkstra with priority queue in 2024:16
* Topological sort of a graph (Kahn's algorithm) in 2025:11b
* OR-tools cp_model in 2025:10b and 2022:15b-ortools
* Shapely in 2025:9b, 2023:18, 2023:10
* Sympy in 2023:24b
* NetworkX in 2023:25

## 2025

1. **Secret Entrance** – Simulate left/right rotations on a 0–99 dial starting at 50 and count how often it ends up at 0 (then, how often it passes 0).
2. **Gift Shop** – From numeric ID ranges, find numbers that are exact repeats of a digit chunk (and then any whole‑chunk repetition) and sum them.
3. **Lobby** – Pick specific digits from strings (batteries) to form the largest possible numbers using greedy optimization.
4. **Printing Department** – On a grid of paper rolls, count rolls accessible to a forklift—those with fewer than four neighbors in the eight surrounding cells.
5. **Cafeteria** – Given inclusive “fresh” ID ranges and a list of ingredient IDs, count how many IDs fall in any fresh range (handling overlaps).
6. **Trash Compactor** – Transpose a matrix of numbers and apply column-specific mathematical operations (addition or multiplication) to find the total value.
   * Complexity in matrix operations and whitespace
7. **Laboratories** – Simulate a downward-moving beam and calculate how many times it splits upon hitting obstacles.
   * Memoization and bottom up calculations
8. **Playground** – Model junction boxes and circuits to identify the three largest connected groups based on physical distance.
9. **Movie Theater** – Calculate areas between pairs of points and determine if specific rectangles fall "out of bounds" of a polygon.
   * Find largest rectangle within ploygon. Used shapely.
10. **Factory** – Find the minimum number of button presses (using XOR logic) required to reach a target state for a machine.
    * Used OR-tools
11. **Reactor** – In a directed device graph, count all paths from node `you` to node `out` (no back edges).
    * Multiple approaches: recursive with memoization, reverse walk and sub paths.
12. **Christmas Tree Farm** – Determine if gift pieces can fit into a restricted regional area.
    * Can be solved using simple area calculations.

## 2024

1. **Historian Hysteria** – Reconcile two lists: first by summing pairwise distances after sorting; then by a “similarity score” that multiplies each left value by its frequency on the right.
2. **Red‑Nosed Reports** – Count sequences that are strictly monotonic with step sizes 1–3; then allow removing one level to “repair” an unsafe report.
3. **Mull It Over** – Extract valid `mul(X,Y)` instructions from corrupted text; then respect `do()`/`don't()` toggles to decide which multiplications count.
4. **Ceres Search** – Find all occurrences of `XMAS` in a letter grid (any direction); then count “X‑shaped” `MAS` patterns formed by two diagonals.
5. **Print Queue** – Apply ordering rules `X|Y` to check if page updates are in valid topological order (sum middles); then fix invalid updates via topo‑sort and rescore.
6. **Guard Gallivant** – Simulate a guard walking with right‑turns on obstacles to count distinct visited tiles; then try placing a single new obstacle to create loops.
7. **Bridge Repair** – For each target, see if numbers can reach it using left‑to‑right `+`/`*`; then add **concatenation** as an operator and recheck.
8. **Resonant Collinearity** – From same‑frequency antennas, mark antinodes aligned with 1:2 spacing; then consider **all harmonics** along the line (including on antennas).
9. **Disk Fragmenter** – Compact a run‑length disk map by sliding blocks left and compute a checksum; then move **whole files** (not blocks) into the first gap that fits.
10. **Hoof It** – Count trailheads (height 0) that can climb to any 9 by steps of +1; then compute a “rating” counting all distinct rising paths.
11. **Plutonian Pebbles** – Repeatedly “blink” numbers by 0→1, split even‑length digit strings, else `×2024`, tracking stone counts; then scale to many more blinks with memoization.
12. **Garden Groups** – For each region of identical crops, price = **area × perimeter**; then compute price using **edge‑runs (“sides”)** instead of raw perimeter.
13. **Claw Contraption** – Find minimal tokens to reach a prize using linear combos of button vectors; then offset prize coordinates by a huge constant and solve the Diophantine system.
14. **Restroom Redoubt** – Move robots on a toroidal grid; after N seconds compute a quadrant safety factor; then find the time when they visually form a message.
15. **Warehouse Woes** – Simulate a robot pushing boxes on a map and sum GPS coordinates; then split each box into a **two‑cell** crate and repeat with push physics.
16. **Reindeer Maze** – Shortest path where steps cost 1 and quarter‑turns cost 1000; then count tiles that lie on **any** optimal route.
    * Created generic Dijkstra's algorithm. Including finding all optimal routes and reverse path calculations.
17. **Chronospatial Computer** – Emulate an 8‑opcode, 3‑bit program and print outputs; then search for a register value that makes the program output its own code.
18. **RAM Run** – Drop bytes that block cells and find the shortest path after N bytes; then identify the **first byte index** at which no path remains.
    * Breadth‑First Search (BFS). Minimum number of steps in grid with N obstacles. Find first obstacle that prevents a path.
19. **Linen Layout** – Given small stripe patterns, count which long designs are **possible**; then count **how many ways** each design can be assembled (DP).
    * Memoization
20. **Race Condition** – Baseline shortest path; then allow one “cheat” through walls for up to 2 steps (later 20) and count cheats that save at least a threshold.
    * Maze where 1 or N steps can be taken ignoring walls
21. **Keypad Conundrum** – Nesting robots translate numeric codes via **directional keypads**; find minimal press length with recursion/memoization; then scale to **25** robots.
    * Controlling numpad through 2 or 25 dirpads. Memoization.
22. **Monkey Market** – Evolve pseudorandom secrets to prices; sum buyers’ 2000th secrets; then pick the best 4‑change price pattern to maximize bananas across buyers.
    * Find optimal sub-sequence in list
23. **LAN Party** – Count all **triangles** (3‑cliques) that include a computer starting with `t`; then output the **maximum clique** as a comma‑sorted list.
    * Solved together with Peter
24. **Crossed Wires** – Simulate a combinational logic network to read a multi‑bit `z` value; then identify which output wires are **mis‑wired** (swap list) to fix addition.
    * Recreated a full binary adder to detect swapped connections
25. **Code Chronicle** – Convert ASCII lock/key schematics to column heights and count every pair whose columns **don’t overlap**

* topo‑sort for Day 5, memoization for 11/21, BFS/Dijkstra variants for 16/18/20/23

## 2023

1. **Trebuchet?!** Recover each line’s calibration value by concatenating its first and last digit (then including spelled‑out numbers) and sum them.
2. **Cube Conundrum** Check which games are possible under RGB cube limits, then compute the “power” as the product of each game’s minimum required cubes.
3. **Gear Ratios** Sum all numbers that touch a symbol in the schematic; then for each gear `*`, multiply its two adjacent numbers and sum those products.
4. **Scratchcards** Score cards where matches double the value per match, then simulate the copy cascade to count how many cards you end up with.
5. **If You Give A Seed A Fertilizer** Chain range‑mapping tables from seeds to locations and find the smallest location (scaling up to huge seed ranges in part two).
6. **Wait For It** For each race time, count the button‑hold durations that beat the record; then repeat for one massive concatenated race.
7. **Camel Cards** Rank five‑card hands and total bids—then re‑rank treating `J` as a wildcard.
8. **Haunted Wasteland** Follow repeated L/R instructions through a labeled graph to reach targets; then synchronize multiple starts by leveraging cycle lengths.
9. **Mirage Maintenance** Use successive differences to extrapolate sequences forward, then backward, and sum the results.
10. **Pipe Maze** Identify and traverse the main pipe loop from `S` to get the farthest step count and the number of enclosed tiles.
11. **Cosmic Expansion** Expand empty rows/columns and sum pairwise galaxy distances—then redo with a much larger expansion factor.
12. **Hot Springs** Count how many `?` replacements yield the listed damaged‑group sizes, then solve again after duplicating the pattern five times (DP).
13. **Point of Incidence** Find perfect vertical or horizontal reflection lines in rock/ash patterns, then allow one smudge.
14. **Parabolic Reflector Dish** Tilt a platform so round rocks roll and compute the north load; then simulate repeated tilt cycles to get the final load.
15. **Lens Library** Implement a custom HASH and simulate labeled lenses in boxes to compute the overall focusing power.
16. **The Floor Will Be Lava** Trace laser beams through mirrors and splitters to count energized tiles; then maximize over all possible starting edges.
17. **Clumsy Crucible** Find a least‑heat‑loss path with limits on straight runs; then solve the “ultra‑crucible” variant with longer run constraints.
18. **Lavaduct Lagoon** Convert trench moves into area/volume to compute lagoon capacity, then decode the hex‑encoded instructions for the large case.
19. **Aplenty** Evaluate rule‑based workflows to sum accepted parts, then count all rating combinations that get accepted by exploring range splits.
20. **Pulse Propagation** Simulate a network of flip‑flops and conjunctions to tally low/high pulses, then deduce the button‑press cycle needed for a condition.
21. **Step Counter** Count garden plots reachable in exactly $$K$$ steps, then extrapolate on an infinite periodic tiling using parity and growth patterns.
22. **Sand Slabs** Let 3D bricks settle under gravity and analyze supports to count safely disintegrable bricks and cascade sizes when removing one brick.
    * Used classes to model state of supporting bricks
23. **A Long Walk** Find the longest simple path on a slope‑constrained trail map; then ignore slopes, compress junctions to a graph, and maximize again.
    * Used AI to cut down computation time
24. **Never Tell Me The Odds** Count pairs of 2D path intersections within bounds, then solve for the single rock (position/velocity) that intersects all hailstones in 3D.
    * Deep dive with Plücker coordinates. Much easier solution with sympy::solve.
25. **Snowverload** Remove exactly three edges (a min 3‑cut) to split the wiring graph in two and multiply the component sizes.
    * Only found solution using NetworkX.

## 2022

1. **Calorie Counting:** Sum calories per Elf and report the largest total, then the sum of the top three.
2. **Rock Paper Scissors:** Score RPS rounds from a guide, then reinterpret the second column as the desired outcome.
3. **Rucksack Reorganization:** Find the common item in each sack’s halves (then in each group of three) and sum its priority.
4. **Camp Cleanup:** Count assignment pairs with full containment, then any overlap, between two numeric ranges.
5. **Supply Stacks:** Simulate crate moves between stacks where order is reversed (then preserved) during transfers.
6. **Tuning Trouble:** Locate the first positions of a 4‑char and 14‑char window of all distinct characters in a stream.
7. **No Space Left On Device:** Parse a terminal transcript, compute directory sizes, then choose the smallest deletion to free enough space.
8. **Treetop Tree House:** Count trees visible from the edges and compute each tree’s “scenic score” from viewing distances.
9. **Rope Bridge:** Simulate a rope following moves and count unique tail positions for a 2‑knot and 10‑knot rope.
10. **Cathode‑Ray Tube:** Track signal strength at specific cycles and render a CRT sprite moving across the screen over time.
11. **Monkey in the Middle:** Pass items between monkeys applying operations; use division/mod tricks to manage worry levels and multiply busiest counts.
12. **Hill Climbing Algorithm:** Find shortest paths on a heightmap under climb constraints from S→E, then from any lowest‑elevation square.
13. **Distress Signal:** Compare nested list packets for ordering and use divider packets to compute a decoder key.
14. **Regolith Reservoir:** Drop sand grains with obstacles until they fall into the abyss, then with a floor to find the final resting count.
15. **Beacon Exclusion Zone:** Using sensor–beacon Manhattan radii, count impossible positions on a row and find the hidden beacon’s tuning frequency.
16. **Proboscidea Volcanium:** Maximize released pressure by opening valves on a graph within time—solo first, then cooperating with an “elephant.”
17. **Pyroclastic Flow:** Drop jet‑pushed rock shapes into a chamber and predict tower height (leveraging cycle detection for huge counts).
18. **Boiling Boulders:** Compute total and exterior surface areas of a voxel lava droplet via adjacency and flood‑fill.
19. **Not Enough Minerals:** Optimize robot‑building choices over time to maximize geodes with careful state pruning/search.
20. **Grove Positioning System:** “Mix” a circular list by element values and read grove coordinates (repeat with a decryption key and many rounds).
21. **Monkey Math:** Evaluate a monkey expression tree, then solve for the unknown input that balances both sides.
22. **Monkey Map:** Follow movement instructions on a 2D map with wrapping, then wrap edges as a cube net for 3D transitions.
23. **Unstable Diffusion:** Simulate elves proposing moves by rotating direction priorities; count empty tiles after 10 rounds and find convergence round.
24. **Blizzard Basin:** Pathfind through a valley with moving blizzards—go start→goal, back, and again—minimizing time.
25. **Full of Hot Air:** Convert and sum numbers in a custom balanced base‑5 (“SNAFU”) system and output the result in SNAFU.

## 2021

1. **Sonar Sweep:** Count how often depth measurements increase (and then using a sliding window).
2. **Dive!:** Follow a list of `forward`, `down`, `up` commands to compute final horizontal position × depth (with “aim” in part 2).
3. **Binary Diagnostic:** Derive power/oxygen/CO₂ ratings by bit‑criteria across binary diagnostics.
4. **Giant Squid:** Simulate bingo boards and compute the score for the first and last winners.
5. **Hydrothermal Venture:** Map line segments (incl. diagonals in part 2) and count points where at least two lines overlap.
6. **Lanternfish:** Model exponentially growing fish with internal timers to count population after many days.
7. **The Treachery of Whales:** Find alignment position minimizing total fuel (linear, then triangular cost).
8. **Seven Segment Search:** Deduce scrambled seven‑segment wiring from patterns to decode outputs.
9. **Smoke Basin:** Identify low points and basin sizes on a heightmap to score risk and largest basins.
10. **Syntax Scoring:** Use a stack to detect corrupted/incomplete bracket lines and compute two scores.
11. **Dumbo Octopus:** Step a 10×10 grid’s energy levels; chain‑react flashes and find the first synchronized step.
12. **Passage Pathing:** Count paths through a cave graph with small‑cave visitation rules (and one small cave twice in part 2).
13. **Transparent Origami:** Fold a dot paper along given axes and read the final code/visualization.
14. **Extended Polymerization:** Apply pair‑insertion rules efficiently (pair counts) to track element frequencies over many steps.
15. **Chiton:** Find a minimum‑risk path on a weighted grid (expanded 5× in part 2).
16. **Packet Decoder:** Parse a hierarchical BITS transmission and evaluate the encoded expression.
17. **Trick Shot:** Simulate projectile motion with drag/gravity to hit a target area and count valid velocities.
18. **Snailfish:** Implement “explode”/“split” reductions and magnitude to sum nested pair numbers.
19. **Beacon Scanner:** Align 3D scanners under rotations/translations to unify beacons and compute distances.
20. **Trench Map:** Repeatedly enhance an infinite image using a 3×3 kernel lookup algorithm.
21. **Dirac Dice:** Play a deterministic dice game, then count wins over branching quantum universes.
22. **Reactor Reboot:** Apply on/off cuboid steps (bounded then unbounded) to count lit cubes via cuboid set algebra.
23. **Amphipod:** Search the state space to organize amphipods into rooms with minimal energy.
24. **Arithmetic Logic Unit:** Analyze/execute a stack‑like ALU program to find the largest/smallest valid model number.
25. **Sea Cucumber:** Simulate east/south‑moving cucumbers until the grid reaches a steady state.

## 2020

1. **Report Repair:** Find the pair (then triple) of expense entries that sum to **2020** and return their product.
2. **Password Philosophy:** Validate passwords under two policies—first by character counts, then by “exactly one of two positions” rules.
3. **Toboggan Trajectory:** Count trees you hit while traversing a repeating map on given slopes, then multiply the counts.
4. **Passport Processing:** Check passports first for required fields, then for stricter field‑value validation.
5. **Binary Boarding:** Decode boarding passes via binary space partitioning to find the highest seat ID and your missing seat.
6. **Custom Customs:** For each group, count questions answered “yes” by anyone, then by everyone, and sum the totals.
7. **Handy Haversacks:** Parse bag‑containment rules to count colors that can hold **shiny gold**, then total bags inside one.
8. **Handheld Halting:** Run a tiny boot program to detect the accumulator before a loop, then fix it by swapping one **jmp/nop**.
9. **Encoding Error:** Find the first number not a sum of two of the previous N numbers, then the contiguous range that sums to it.
10. **Adapter Array:** Compute 1‑jolt × 3‑jolt difference counts, then count all valid adapter arrangements.
11. **Seating System:** Simulate seat occupancy until stable—first with adjacency, then with line‑of‑sight rules.
12. **Rain Risk:** Follow navigation actions; part two steers using a moving waypoint relative to the ship.
13. **Shuttle Search:** Find best bus ID × wait time, then the earliest timestamp matching bus offsets (CRT style).
14. **Docking Data:** Apply bitmasks to values on writes, then to addresses with floating **X** bits to sum memory.
15. **Rambunctious Recitation:** Play the memory game to determine the 2020th and 30,000,000th spoken numbers.
16. **Ticket Translation:** Identify invalid ticket values, then deduce field positions and multiply “departure” fields.
17. **Conway Cubes:** Run a 3D (then 4D) Game‑of‑Life‑style automaton for six cycles and count active cubes.
18. **Operation Order:** Evaluate arithmetic with nonstandard precedence (left‑to‑right), then with **+** before **×**.
19. **Monster Messages:** Validate messages against a rule grammar; part two introduces recursive rules.
20. **Jurassic Jigsaw:** Reassemble image tiles by matching borders, then find sea monsters and compute roughness.
21. **Allergen Assessment:** Map allergens to unique ingredients; count safe appearances and list dangerous ingredients.
22. **Crab Combat:** Simulate a two‑deck card game; part two uses recursive combat; compute winner’s score.
23. **Crab Cups:** Perform cup moves on a circular list (100 moves), then scale to 1,000,000 cups and 10,000,000 moves.
24. **Lobby Layout:** Flip hex tiles based on path instructions, then evolve daily by neighbor rules.
25. **Combo Breaker:** Recover loop sizes from public keys to derive the shared encryption key (no part two).

## 2019

1. **The Tyranny of the Rocket Equation** Sum fuel for each module mass; then include fuel needed for the fuel itself recursively.
2. **1202 Program Alarm** Run a minimal Intcode (add/multiply/halt) and find the noun/verb that produce a target output.
3. **Crossed Wires** Trace two grid wires to find the closest intersection by Manhattan distance, then the least combined steps.
4. **Secure Container** Count six‑digit passwords in a range with non‑decreasing digits and a required double; part two demands an exact pair.
5. **Sunny with a Chance of Asteroids** Extend Intcode with input/output and parameter modes to run diagnostics.
6. **Universal Orbit Map** Compute total direct+indirect orbits; then find orbital transfers between YOU and SAN.
7. **Amplification Circuit** Chain five Intcode amplifiers (and later a feedback loop) to maximize thruster signal over phase settings.
8. **Space Image Format** Decode a layered image to get a checksum (fewest zeros layer) and render a visible message with transparency rules.
9. **Sensor Boost** Add relative‑base addressing and large memory to Intcode; run BOOST to output required keycodes.
10. **Monitoring Station** Pick the asteroid with the most visible asteroids; then vaporize them with a rotating laser to find a specific hit.
11. **Space Police** Simulate an Intcode‑driven hull‑painting robot to count painted panels and read the painted registration identifier.
12. **The N‑Body Problem** Simulate gravity between moons to get total energy after N steps and the system’s repeat period via per‑axis cycles.
13. **Care Package** Run the Intcode arcade to count block tiles, then play automatically to break all blocks and report the score.
14. **Space Stoichiometry** Given chemical reactions, compute ORE needed for 1 FUEL and the max FUEL producible from a fixed ORE budget.
15. **Oxygen System** Explore an unknown maze with a remote Intcode droid to find the shortest path to oxygen and time to flood the area.
16. **Flawed Frequency Transmission** Apply an FFT‑like transform over many phases to extract an 8‑digit message, optimizing for huge inputs.
17. **Set and Forget** From an ASCII scaffold map compute the alignment parameter sum, then compress movement into routines to collect dust.
18. **Many‑Worlds Interpretation** In a keys‑and‑doors labyrinth, find the shortest steps to gather all keys; part two splits the vault among four robots.
19. **Tractor Beam** Probe a coordinate grid with Intcode to count affected points and locate the nearest 100×100 square fully inside the beam.
20. **Donut Maze** Find the shortest path through a portal‑labeled maze, then solve the recursive layered version.
21. **Springdroid Adventure** Write compact boolean “springscript” to decide when to jump so the droid survives in WALK and RUN modes.
22. **Slam Shuffle** Model shuffles (new stack, cut, deal with increment) as modular linear transforms to track a card under huge decks/iterations.
23. **Category Six** Simulate 50 networked Intcode computers (with a NAT) to find the first Y sent to 255 and the first repeated NAT Y on idle.
24. **Planet of Discord** Evolve a 5×5 bug grid to the first repeated biodiversity layout, then run multi‑level recursive grids for a minute count.
25. **Cryostasis** Play a text‑adventure via Intcode to find the right item combination to pass a pressure sensor and obtain the passcode.

## 2018

1. **Chronal Calibration:** Sum frequency changes, then loop the list to find the first frequency you reach twice.
2. **Inventory Management System:** Compute a checksum from box ID letter counts, then find the two IDs that differ by exactly one character and extract their common letters.
3. **No Matter How You Slice It:** Determine overlapping square inches among fabric claims and identify the single claim that doesn’t overlap any other.
4. **Repose Record:** Analyze guards’ minute‑by‑minute sleep logs to find the sleepiest guard/minute combination(s).
5. **Alchemical Reduction:** Repeatedly react adjacent opposite‑polarity units in a polymer; then remove one unit type entirely to produce the shortest possible result.
6. **Chronal Coordinates:** Using Manhattan distance, find the largest finite area closest to a coordinate and the size of the “safe region” below a total‑distance threshold.
7. **The Sum of Its Parts:** Topologically order steps with alphabetical tie‑breaks; then simulate multiple workers with step durations.
8. **Memory Maneuver:** Parse a tree from a flat number stream; sum all metadata and compute the root node’s value by child‑referencing rules.
9. **Marble Mania:** Simulate a circular marble game with special scoring on multiples of 23 to compute the highest score.
10. **The Stars Align:** Advance points with velocities until they form legible letters; report the message and when it appears.
11. **Chronal Charge:** On a 300×300 grid, find the 3×3 and any‑size square with the highest total power (often via summed‑area tables).
12. **Subterranean Sustainability:** Evolve plant pots as a 1‑D cellular automaton over many generations; sum the indices of pots containing plants (extrapolating long‑term growth).
13. **Mine Cart Madness:** Simulate carts moving on tracks with curves and intersections to find the first crash and the location of the last remaining cart.
14. **Chocolate Charts:** Build a recipe scoreboard to get the ten scores after a given count and find where a target sequence first appears.
15. **Beverage Bandits:** Simulate Elf vs. Goblin combat on a grid with reading‑order rules; compute the outcome and the minimum Elf attack boost with no Elf deaths.
16. **Chronal Classification:** Deduce mappings from opcode numbers to behaviors using samples, then execute the device program with the discovered mapping.
17. **Reservoir Research:** Simulate water flowing through clay veins to count tiles the water reaches and the amount retained.
18. **Settlers of The North Pole:** Run a cellular automaton on a forest grid to compute resource value after a given time (spotting and exploiting cycles for large steps).
19. **Go With The Flow:** Execute an assembly‑like program with a register‑bound instruction pointer; analyze/optimize to derive the final register value efficiently.
20. **A Regular Map:** Parse a regex of N/S/E/W moves with branching to construct a room‑and‑door graph, then find the furthest distance and rooms beyond a threshold.
21. **Chronal Conversion:** Reverse‑engineer a program tied to the instruction pointer to find the lowest initial value that halts quickly and the value that halts last.
22. **Mode Maze:** Generate terrain types and risks from erosion math, then use pathfinding with tool switches to reach the target in minimal time.
23. **Experimental Emergency Teleportation:** With 3‑D nanobots using Manhattan ranges, count bots in range of the strongest one and find the point maximizing in‑range bots nearest the origin.
24. **Immune System Simulator 20XX:** Simulate target selection and attacks between two armies to determine surviving units and the minimum boost for an immune‑system win.
25. **Four‑Dimensional Adventure:** Group 4‑D points into constellations where pairwise Manhattan distance ≤ 3 (or reachable by such chains) and count the constellations.

## 2017

1. **Inverse Captcha** Sum digits that match the next digit in a circular list; then sum digits matching the digit halfway around.
2. **Corruption Checksum** For each row, take `max−min` and sum; then find the only evenly divisible pair per row and sum the quotients.
3. **Spiral Memory** Compute Manhattan distance to 1 in a square spiral; then generate neighbor‑sum values and return the first exceeding the input.
4. **High‑Entropy Passphrases** Count passphrases with no duplicate words; then also reject any that contain anagrams.
5. **A Maze of Twisty Trampolines, All Alike** Walk a list of jump offsets, modifying them as you go; second part lowers large offsets (≥3) instead of incrementing.
6. **Memory Reallocation** Repeatedly redistribute blocks among banks until a configuration repeats; then report the loop length.
7. **Recursive Circus** Identify the bottom program of a tower; then find the misweighted program and the correction needed to balance.
8. **I Heard You Like Registers** Execute conditional register operations, tracking the largest value at the end and the highest value ever seen.
9. **Stream Processing** Parse nested groups and garbage to score groups; then count non‑canceled characters within garbage.
10. **Knot Hash** Perform the knotting algorithm to get a simple product; then run 64 rounds and output the dense hash as hexadecimal.
11. **Hex Ed** Follow hex‑grid steps and compute the final distance; then track the maximum distance reached at any point.
12. **Digital Plumber** Build an undirected graph to find the size of the group containing program 0; then count all connected components.
13. **Packet Scanners** Simulate a layered firewall to compute severity; then find the smallest delay that avoids all detections.
14. **Disk Defragmentation** Use knot hashes to build a 128×128 usage grid and count used squares; then count connected regions.
15. **Dueling Generators** Compare the low 16 bits of two pseudo‑random sequences; then apply “picky” divisibility filters before comparing.
16. **Permutation Promenade** Apply spin/exchange/partner dance moves to a line of programs; then exploit cycle detection to repeat a billion times.
17. **Spinlock** Perform circular insertions after a fixed step count and report the value after the last insert; then, for huge iterations, report the value after 0 without building the buffer.
18. **Duet** Execute a small assembly to recover the last played sound; then run two programs concurrently and count how many sends program 1 performs.
19. **A Series of Tubes** Traverse an ASCII pathway, collecting letters along the route; then also count total steps taken.
20. **Particle Swarm** Determine the particle that stays closest to the origin in the long run; then simulate and remove particles that collide.
21. **Fractal Art** Repeatedly enhance a pixel pattern using transformation rules; then count lit pixels after more iterations.
22. **Sporifica Virus** Move a virus carrier on a grid, turning and flipping infection states; then use a four‑state model (clean/weak/infected/flagged).
23. **Coprocessor Conflagration** Run an assembly program and count `mul` instructions; then analyze/translate to count non‑primes over a range.
24. **Electromagnetic Moat** Build bridges from port pairs to maximize total strength; then among the longest bridges, pick the strongest.
25. **The Halting Problem** Simulate a described Turing machine for a set number of steps and output the resulting checksum.

## 2016

1. **No Time for a Taxicab** Follow L/R turn + step instructions on a grid to get Manhattan distance; then find the **first location visited twice**.
2. **Bathroom Security** Walk a keypad by U/D/L/R to read a code; then repeat on a **diamond‑shaped** keypad.
3. **Squares With Three Sides** Count valid triangles by row; then read the input **by columns** (groups of three) and recount.
4. **Security Through Obscurity** Validate room names with checksums and sum sector IDs; then **decrypt via Caesar shift** to find the “northpole” storage.
5. **How About a Nice Game of Chess?** Brute‑force MD5 hashes to build an 8‑char password; then fill positions using the **6th hex nibble as an index**.
6. **Signals and Noise** Recover a message by taking the **most common** letter in each column; then the **least common** letters.
7. **Internet Protocol Version 7** Detect TLS (ABBA outside brackets, none inside); then SSL (ABA outside with **matching BAB inside**).
8. **Two‑Factor Authentication** Simulate a 50×6 pixel screen with `rect` and row/column rotations; then read the **letters** displayed.
9. **Explosives in Cyberspace** Decompress strings with marker syntax `AxB`; then compute **recursive** decompressed length without expanding.
10. **Balance Bots** Simulate bots comparing chips to find who compares target values; then multiply outputs in bins **0,1,2**.
11. **Radioisotope Thermoelectric Generators** Move paired microchips/generators by elevator under safety rules to reach the top in **fewest steps**.
12. **Leonardo’s Monorail** Run simple **Assembunny** code to get a register value; then rerun with a different initial state.
13. **A Maze of Twisty Little Cubicles** On a formula‑generated maze, find the shortest path to a target; then count locations reachable in **≤50** steps.
14. **One‑Time Pad** Produce keys where MD5 has a **triple** followed by a **quintuple** within 1000 hashes; then use **stretched** hashing.
15. **Timing Is Everything** Find the earliest time a ball passes all rotating discs’ slots; then solve again with an **extra disc**.
16. **Dragon Checksum** Expand bits via the **dragon** rule to a target length and compute a checksum; then for a much larger disk.
17. **Two Steps Forward** In a 4×4 maze whose **open doors** come from MD5(passcode+path), find shortest path; then the **longest path length**.
18. **Like a Rogue** Generate rows of traps/safe tiles from neighbors and count safe tiles after **40** rows; then after **400,000** rows.
19. **An Elephant Named Joseph** Solve a Josephus variation (steal from neighbor); then a second variant (steal from the **opposite** elf).
20. **Firewall Rules** Merge blocked IP intervals to find the **lowest allowed** IP; then count **all** allowed IPs.
21. **Scrambled Letters and Hash** Apply string‑scrambling operations to get the result; then **invert** the operations to unscramble.
22. **Grid Computing** Count “viable pairs” of storage nodes; then slide the empty node to move the **goal data** to (0,0) in minimal steps.
23. **Safe Cracking** Run Assembunny with **toggle** instruction, then optimize/recognize it computes a math result for large initial values.
24. **Air Duct Spelunking** On a maze, compute the shortest route visiting all numbered POIs (TSP); then return to the **start**.
25. **Clock Signal** Find the smallest initial register that makes the program output an **alternating 0/1** clock signal indefinitely.

## 2015

1. **Not Quite Lisp** — Track `(` / `)` to get Santa’s final floor, then find the first character position that enters the basement.
2. **I Was Told There Would Be No Math** — Sum wrapping paper (surface area + smallest side) and ribbon (smallest perimeter + bow) needs for all boxes.
3. **Perfectly Spherical Houses in a Vacuum** — Count unique houses visited from `^v<>` moves; then repeat with Robo‑Santa alternating steps.
4. **The Ideal Stocking Stuffer** — Find the smallest integer that makes an MD5(secret+N) start with five zeroes; then six.
5. **Doesn’t He Have Intern‑Elves For This?** — Classify strings as “nice” by vowel/double/blacklist rules; then by pair‑twice + repeat‑with‑gap rules.
6. **Probably a Fire Hazard** — Simulate a 1000×1000 light grid with on/off/toggle; then track **brightness** with +1/−1/+2 rules.
7. **Some Assembly Required** — Evaluate a 16‑bit wire/gate circuit to get the signal on wire `a`; then override `b` with that value and recompute.
8. **Matchsticks** — Compute code‑chars minus in‑memory chars across string literals; then compute encoded‑chars minus code‑chars.
9. **All in a Single Night** — Find the shortest Hamiltonian route (TSP) over city distances; then the **longest**.
10. **Elves Look, Elves Say** — Apply the look‑and‑say transform repeatedly and report the string length after 40 rounds, then 50.
11. **Corporate Policy** — Increment an 8‑letter password until it meets straight/no‑iol/two‑pairs rules; then find the next valid one again.
12. **JSAbacusFramework.io** — Sum all numbers in a JSON document; then ignore any **object** containing the value `"red"`.
13. **Knights of the Dinner Table** — Arrange circular seating to maximize total happiness; then include **yourself** with neutral edges.
14. **Reindeer Olympics** — Simulate flying/resting to find the farthest reindeer after 2503 s; then award per‑second lead points and find the top scorer.
15. **Science for Hungry People** — Allocate 100 tsp of ingredients to maximize the cookie score; then constrain total calories to 500.
16. **Aunt Sue** — Identify which Aunt Sue matches the MFCSAM clues; then reinterpret four properties as greater/less‑than instead of equals.
17. **No Such Thing as Too Much** — Count ways container sizes can sum to 150 liters; then count ways using the **fewest** containers.
18. **Like a GIF For Your Yard** — Run Conway‑style lights for 100 steps; then repeat with the four **corner lights stuck on**.
19. **Medicine for Rudolph** — Count distinct molecules after one replacement; then find the **minimum steps** to build the medicine from `e`.
20. **Infinite Elves and Infinite Houses** — Find the lowest house reaching a present threshold (10×sum of divisors); then with elves stopping after 50 houses (11×).
21. **RPG Simulator 20XX** — Choose shop items to **win** with minimum gold; then the most gold you can spend and still **lose**.
22. **Wizard Simulator 20XX** — Spend minimal mana to defeat the boss with timed spell effects; then do it again on **Hard** (lose 1 HP every player turn).
23. **Opening the Turing Lock** — Execute a two‑register program and report `b`; then rerun with register `a` initialized to 1.
24. **It Hangs in the Balance** — Partition packages into 3 equal‑weight groups minimizing first‑group size, breaking ties by **quantum entanglement**; then into 4 groups.
25. **Let It Snow** — Walk diagonals of a code grid to your row/col and generate the code via modular multiplication sequence.
