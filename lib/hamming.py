# encoding: utf-8
import sys
import copy

from unionfind import UnionFind

def hamming_neighbours(x, dist=1, radix=24):
    ret = set()
    for i in range(radix):
        y = x ^ 2**i
        ret.add(y)
        if dist > 1:
            ret = ret | hamming_neighbours(y, dist-1, radix)
    return ret


def cluster(vertices, radix):
    V = frozenset(vertices)
    u = UnionFind()
    for v in V:
        u.add(v)
    print "Starting with {} clusters".format(u.clusters)
    i = 0.0
    for v in V:
        if i % 100 == 0:
            p = 100*( i / len(vertices))
            sys.stdout.write("\r%f%% (%d)" % (p, len(V)))
            sys.stdout.flush()
        potential = hamming_neighbours(v, radix=radix, dist=2)
        for p in potential:
            if p in V:
                neighbour = p
                u.union(v, neighbour)

        i += 1
    sys.stdout.write("\n")
    return u


###
## Parsing
##
def _parse_header(f):
    line = f.readline().strip()
    num_vertices, radix = line.split(' ')
    return int(num_vertices), int(radix)

def _parse_vertex(line, radix):
    """ Input: String if type '0 1 1 0 1', 5 """
    bits = line.split(' ')
    assert len(bits) == radix
    return int(''.join(bits), 2)

def parse(f):
    num_vertices, radix = _parse_header(f)
    print "Parsing {} ints of size {}".format(num_vertices, radix)
    ret = set()
    dupes = set()
    for row in range(num_vertices):
        vertex = _parse_vertex(f.readline().strip(), radix)
        if vertex in ret:
            dupes.add(vertex)
        ret.add(vertex)
    print "Found {} dupes".format(len(dupes))
    return ret, radix
