# compiler setup
CC=g++
CFLAGS=-Ofast

# define targets
TARGETS=chains_simple chains_optimised Hopcroft_Karp_Karzanov Edmonds_Karp

#define object-files
OBJ=chains_simple.o chains_optimised.o Hopcroft_Karp_Karzanov.o Edmonds_Karp.o

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
