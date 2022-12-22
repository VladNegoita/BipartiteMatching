# compiler setup
CXX=g++
CXXFLAGS=-Ofast

# define targets
TARGETS=chains_simple chains_optimised Hopcroft_Karp_Karzanov Edmonds_Karp check

simple: build

run-best: run-p2

run-p1: chains_simple
	./chains_simple

run-p2: chains_optimised
	./chains_optimised

run-p3: Hopcroft_Karp_Karzanov
	./Hopcroft_Karp_Karzanov

run-p4: Edmonds_Karp
	./Edmonds_Karp

build: $(TARGETS)

pack:
	zip -FSr vlad_andrei.negoita.zip Readme.md Makefile *.cpp *.py *.pdf in out

clean:
	rm -f $(TARGETS)

.PHONY: pack clean
