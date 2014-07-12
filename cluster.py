# encoding: utf-8
from heapq import heappush, heappop
from unionfind import UnionFind

def heapify(edges):
    X = []
    for edge in edges:
        heappush(X, (edge.cost, edge))
    return X


def cycle(union, edge):
    l0 = union.find(edge.v0)
    l1 = union.find(edge.v1)
    return l0 == l1


def get_mindist(u, edges):
    cost, edge = heappop(edges)
    while cycle(u, edge):
        cost, edge = heappop(edges)
    return cost


def cluster(graph, k):
    edges = heapify(graph.edges)

    u = UnionFind()
    [u.add(node) for node in graph.nodes.values()]

    while u.clusters > k:
        cost, edge = heappop(edges)
        if cycle(u, edge):
            #print "skipping {}".format(edge)
            pass
        else:
            u.union(u.find(edge.v0), u.find(edge.v1))

    mindist = get_mindist(u, edges)
    return mindist, u.followers
