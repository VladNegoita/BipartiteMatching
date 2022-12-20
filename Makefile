# compiler setup
CC=g++
CFLAGS=-Ofast

# define targets
TARGETS=chains_simple chains_optimised Hopcroft_Karp_Karzanov Edmonds_Karp

#define object-files
OBJ=chains_simple.o chains_optimised.o Hopcroft_Karp_Karzanov.o Edmonds_Karp.o

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

image_editor: $(OBJ)
	$(CC) $(CFLAGS) *.o -o image_editor

%.o: %.cpp
	$(CC) $(CFLAGS) -c -o $@ $<

pack:
	zip -FSr nume.zip Readme.md Makefile *.cpp *.py *.pdf

clean:
	rm -f $(TARGETS) $(OBJ)
	

.PHONY: pack clean
