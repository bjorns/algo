# coding=utf-8
import heapq
from copy import copy


def heapify(edges):
    X = []
    for edge in edges:
        heapq.heappush(X, (edge.cost, edge))
    return X


def cycle(graph, edge):
    left_inside = edge.v0 in X
    right_inside = edge.v1 in X
    return left_inside and right_inside and something_else


def spanning_tree(graph):
    edges = heapify(graph.edges)
    X = set()
    while len(X) < graph.nodes and len(edges) > 0:
        cost, edge = heapq.heappop(edges)

        cycle = cycle(graph, edge)
        if cycle:
            #print "skipping {}".format(edge)
            pass
        else:
            print "adding {}".format(edge)
            edge.spanning = True
            if not left_inside:
                X.add(edge.v0)
            if not right_inside:
                X.add(edge.v1)
    return graph
