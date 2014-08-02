# encoding: utf-8
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/lib')

import knapsack
import bintree

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "usage: ./homework3.py [1-3] <inputfile>"
        sys.exit(0)
    problem = sys.argv[1]
    filename = sys.argv[2]

    f = open(filename, 'r')
    if problem == '1':
        items, capacity = knapsack.parse(f)
        print knapsack.solve(items, capacity)
    elif problem == '2':
        pass
    elif problem == '3':
        items = bintree.parse(f)
        print bintree.solve(items)
