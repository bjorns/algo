all: quicksort redblack.png

clean:
	rm -f redblack.png redblack.dot redblack quicksort

quicksort: legacy/quicksort.c
	mkdir -p bin
	gcc -Wall --std=c99 -o bin/quicksort $^

redblack: legacy/redblack.c
	gcc -Wall --std=c99 -o $@ $^

redblack.dot: redblack
	./redblack

redblack.png: redblack.dot
	dot -Tpng -o $@ $<

dijkstra:
		python dijkstra.py "New York, New York"
		dot -Tpdf a.dot > a.pdf
		open a.pdf

test:
		PYTHONPATH=lib:test python -m unittest test.test_graphs test.test_unionfind

.PHONY: test
