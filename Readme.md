# BipartiteMatching

## Project Structure

Here you have the hierarchy:

```
.
├── Edmonds_Karp.cpp
├── Hopcroft_Karp_Karzanov.cpp
├── Makefile
├── Readme.md
├── chains_optimised.cpp
├── chains_simple.cpp
├── check.cpp
├── check.py
├── in
│   └── testX.in
├── out
│   └── testX.out
├── performance_analysis.py
├── test.in
├── test.out
└── test_generator.py
```

The source code (programs that solve the bipartite matching problem) are:

1. `Edmonds_Karp.cpp`
2. `Hopcroft_Karp_Karzanov.cpp`
3. `chains_optimised.cpp`
4. `chains_simple.cpp`

`Makefile` compiles the source code and enables running each algoritm on `test.in` and writes the solution in `test.out`.

The files responsible for checking the answer are:

1. `check.cpp` - verifies that the output is correct (not optimal): checks if each printed edge exist in the original graph.

2. `check.py` - runs `check.cpp` for each algorithm and for each test, also comparing the size of the maximum matching (to be equal along any algorithm).

The folders `in/` and `out/` store the input files and their answer, respectively.

The program responsible for ploting and time measurements is `performance_analysis.py`. This script runs each algorithm on each input, records the effective running time and plots those accordingly.

The input files located in `in/` were generated using the script `test_generator.py`.

## Github

You can find this project on [Github](https://github.com/VladNegoita/BipartiteMatching).

