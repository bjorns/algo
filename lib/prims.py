# coding=utf-8
import sys
from copy import copy
import random
import heapq
import heap

def _crossing_frontier(edge, X):
    return (edge.v0 in X and edge.v1 not in X) or \
        (edge.v0 not in X and edge.v1 in X)


def _outside_frontier(edge, X):
    return edge.v0 not in X and edge.v1 not in X


def cost_of(node, X):
    ret = sys.maxint
    for edge in node.edges:
        if edge.cost < ret and _crossing_frontier(edge, X):
            ret = edge.cost
    return ret


def init_frontier(nodes, X):
    frontier = []
    for node in nodes:
        heapq.heappush(frontier, (cost_of(node, X), node))
    return frontier

def _find_crossing_edge(node, X):
    for edge in node.edges:
        if _crossing_frontier(edge, X):
            return edge


def index_positions(frontier):
    ret = dict()
    K = len(frontier)
    for i in range(len(frontier)):
        cost, node = frontier[i]
        ret[node] = i - K
    return ret


def delete_entry(entry, frontier):
    for i, _entry in enumerate(frontier):
        if entry == _entry:
            key, node = _entry
            print "\tDeleting %d: (%d, %s)" % (i, key, node)
            heap.delete_nth(frontier, i)


def spanning_tree(graph, start_node):
    print "Start node: {}".format(start_node)
    X = set([start_node])

    nodes = copy(graph.get_nodes())
    nodes.remove(start_node)

    frontier = init_frontier(nodes, X)
    pos_index = index_positions(frontier)
    print "Frontier: {}".format( frontier)
    while len(frontier) > 0:
        cost, node = heapq.heappop(frontier)
        print "Next node is {}".format(node)
        for edge in node.edges:
            if _crossing_frontier(edge, X) and edge.cost == cost:
                print "Adding spanning edge {}".format(edge)
                edge.spanning = True

        X.add(node)

        for edge in node.edges:
            if _crossing_frontier(edge, X):
                v1 = edge.other_end(node)
                print "Updating frontier for node {}".format(v1)
                key = sys.maxint
                delete_entry((key, v1), frontier)
                new_key = cost_of(v1, X)
                print "\tNew value is (%d,%s)" % (new_key, v1)
                heapq.heappush(frontier, (new_key, v1))
    return X
