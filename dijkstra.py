# coding=utf-8
import sys
from graph import Node, Edge, parse

def cheapest(frontier):
    lowest = -1
    ret = None
    for edge in frontier:
        if lowest == -1 or edge.src.cost + edge.cost < lowest:
            lowest = edge.src.cost + edge.cost
            ret = edge
    return ret


def dijkstra(start, nodes):
    """ Returns a set of all nodes in the graph. """
    ret = set()
    frontier = set()
    start.cost = 0
    for e in start.edges:
        frontier.add(e)
    nodes.remove(start)
    ret.add(start)
    while len(nodes) > 0:
        edge = cheapest(frontier)
        frontier.remove(edge)

        next_node = edge.dst
        next_node.cost = edge.src.cost + edge.cost

        for e in next_node.edges:
            if e.dst in nodes:
                frontier.add(e)

        nodes.remove(next_node)
        ret.add(next_node)
    return ret


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "Usage ./dijkstra <input-file> <start-node>"
        sys.exit(0)
    filename = sys.argv[1]
    start_node = sys.argv[2]
    nodes = parse(filename)

    result = dijkstra(nodes[start_node], set(nodes.values()))
    for node in result:
        print "{}: {}".format(node.name, node.cost)
