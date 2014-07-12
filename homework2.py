# encoding: utf-8
import sys

import graphs
import cluster

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "usage: ./homework2.py [1|2|3] <inputfile>"
        sys.exit(0)
    question = sys.argv[1]
    filename = sys.argv[2]
    param = sys.argv[3]
    if question == '1':
        graph = graphs.parse(filename, undirected=True)
        mindist, clust = cluster.cluster(graph, int(param))
        for key,values in clust.items():
            print "{}:".format(key)
            for v in values:
                print "\t{}".format(v)
        print "Shortest distance: {}".format(mindist)
