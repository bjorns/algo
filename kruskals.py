# coding=utf-8
import heapq
from copy import copy
from unionfind import UnionFind

def heapify(edges):
    X = []
    for edge in edges:
        heapq.heappush(X, (edge.cost, edge))
    return X


def cycle(union, edge):
    l0 = union.find(edge.v0)
    l1 = union.find(edge.v1)
    return l0 == l1


def spanning_tree(graph):
    edges = heapify(graph.edges)
    X = set()
    u = UnionFind()

    [u.add(node) for node in graph.nodes.values()]



    while len(edges) > 0:
        cost, edge = heapq.heappop(edges)

        if cycle(u, edge):
            #print "skipping {}".format(edge)
            pass
        else:
            print "adding {}".format(edge)
            edge.spanning = True
            u.union(u.find(edge.v0), u.find(edge.v1))
    return graph
