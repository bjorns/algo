# encoding: utf-8
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/lib')

import graphs
import allpairs


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "usage: ./homework4.py <inputfile>"
        sys.exit(0)

    filename = sys.argv[1]

    f = open(filename, 'r')
    G = graphs.parse_matrix(f)
    R = allpairs.floyd_warshall(G)
