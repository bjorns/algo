all: quicksort redblack.png

clean:
	rm -f redblack.png redblack.dot redblack quicksort
	
quicksort: quicksort.c
	gcc -Wall --std=c99 -o quicksort quicksort.c

redblack: redblack.c
	gcc -Wall --std=c99 -o $@ $^

redblack.dot: redblack
	./redblack

redblack.png: redblack.dot
	dot -Tpng -o $@ $<
