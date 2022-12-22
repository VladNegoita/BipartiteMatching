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

The files responsible for checking the answer are:

1. `check.cpp` - verifies that the output is correct (not optimal): checks if each printed edge exist in the original graph.

2. `check.py` - runs `check.cpp` for each algorithm and for each test, also comparing the size of the maximum matching (to be equal along any algorithm).

The folders `in/` and `out/` store the input files and their answer, respectively.

The program responsible for ploting and time measurements is `performance_analysis.py`. This script runs each algorithm on each input, records the effective running time and plots those accordingly.

The input files located in `in/` were generated using the script `test_generator.py`.

## Usage

`Makefile` compiles the source code and enables running each algoritm on `test.in` and writes the solution in `test.out`. It has the following rules:

1. `run-best` - runs Hopcroft_Karp_Karzanov
2. `run-pX` - runs each algorithm (X is the corresponding number)
3. `build` - compiles all the `.cpp` files (the algorithms and the `check.cpp`)
4. `pack` - packs the project (for sending via network)
5. `clean` - deletes the executables

## Observations

Here you have 2 important notes:

1. The generated graph is actually called a multigraph (it may have multiple edges between a pair of nodes)

2. There is a small bug in the generation of tests regarding dense graphs: instead of generating about left_set_size * right_set_size edges (asymptotically, of course), the tests were generated with about nodes_count * nodes_count edges. This problem won't impact the analysis of our algorithms since the graph is (now more than it should) dense. The problem will be corrected in teh future.

## Competition

Test ID: 21

## Github

You can find this project on [Github](https://github.com/VladNegoita/BipartiteMatching).

###### Copyright Vlad Negoiță vlad1negoita@gmail.com