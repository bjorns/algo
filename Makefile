all: quicksort

quicksort: quicksort.c
	gcc -Wall --std=c99 -o quicksort quicksort.c
