## F1. Falling Sand (Easy Version)
The difference between the versions is the constraints on 𝑎𝑖. You can make hacks only if all versions of the problem are solved.

Little Dormi has recently received a puzzle from his friend and needs your help to solve it.

The puzzle consists of an upright board with 𝑛 rows and 𝑚 columns of cells, some empty and some filled with blocks of sand, and 𝑚 (𝑚 number od columns) non-negative integers 𝑎1,𝑎2,…,𝑎𝑚 (0≤𝑎𝑖≤𝑛). In this version of the problem, 𝑎𝑖 will be equal to the number of blocks of sand in column 𝑖.

When a cell filled with a block of sand is disturbed, the block of sand will fall from its cell to the sand counter at the bottom of the column (each column has a sand counter). While a block of sand is falling, other blocks of sand that are adjacent at any point to the falling block of sand will also be disturbed and start to fall. Specifically, a block of sand disturbed at a cell (𝑖,𝑗) will pass through all cells below and including the cell (𝑖,𝑗) within the column, disturbing all adjacent cells along the way. Here, the cells adjacent to a cell (𝑖,𝑗) are defined as (𝑖−1,𝑗), (𝑖,𝑗−1), (𝑖+1,𝑗), and (𝑖,𝑗+1) (if they are within the grid). Note that the newly falling blocks can disturb other blocks.

In one operation you are able to disturb any piece of sand. The puzzle is solved when there are at least 𝑎𝑖 blocks of sand counted in the 𝑖-th sand counter for each column from 1 to 𝑚.

You are now tasked with finding the minimum amount of operations in order to solve the puzzle. Note that Little Dormi will never give you a puzzle that is impossible to solve.

### Input
The first line consists of two space-separated positive integers 𝑛 and 𝑚 (1≤𝑛⋅𝑚≤400000).

Each of the next 𝑛 lines contains 𝑚 characters, describing each row of the board. If a character on a line is '.', the corresponding cell is empty. If it is '#', the cell contains a block of sand.

The final line contains 𝑚 non-negative integers 𝑎1,𝑎2,…,𝑎𝑚 (0≤𝑎𝑖≤𝑛) — the minimum amount of blocks of sand that needs to fall below the board in each column. In this version of the problem, 𝑎𝑖 will be equal to the number of blocks of sand in column 𝑖.

### Output
Print one non-negative integer, the minimum amount of operations needed to solve the puzzle.

Examples



### input
```
    5 7
    #....#.
    .#.#...
    #....#.
    #....##
    #.#....
    4 1 1 1 0 3 1
```

### ouput
```
    3
```

### Note
For example 1, by disturbing both blocks of sand on the first row from the top at the first (0,0) and sixth columns (0,5) from the left, and the block of sand on the second row from the top and the fourth column from the left (1,3) , it is possible to have all the required amounts of sand fall in each column. It can be proved that this is not possible with fewer than 3 operations, and as such the answer is 3. Here is the puzzle from the first example.

