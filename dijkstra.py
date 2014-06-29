# coding=utf-8
import sys
from graph import Node, Edge, parse, graphviz, generate

def cheapest(frontier, graph):
    lowest = -1
    ret = None
    for edge in frontier:
        if lowest == -1 or edge.src.cost + edge.cost < lowest:
            if edge.dst in graph:
                lowest = edge.src.cost + edge.cost
                ret = edge
    return ret


def dijkstra(start, graph):
    """ Returns a set of all nodes in the graph. """
    ret = set() # The set 'W' to be returned.
    frontier = set() # All edges crossing into unchecked.
    start.cost = 0
    for e in start.edges:
        frontier.add(e)
    graph.remove(start)
    ret.add(start)
    while len(graph) > 0:
        edge = cheapest(frontier, graph)
        if edge is None:
            break
        frontier.remove(edge)

        next_node = edge.dst
        next_node.cost = edge.src.cost + edge.cost

        for e in next_node.edges:
            if e.dst in graph:
                frontier.add(e)

        graph.remove(next_node)
        ret.add(next_node)
    return ret


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage ./dijkstra <input-file> <start-node>"
        sys.exit(0)
    start_node = sys.argv[1]
    if len(sys.argv) < 3:
        import cities
        nodenames = ["{}, {}".format(city, state) for city, state in cities.CITIES]
        nodes = generate(100, nodenames)
        filename = "a.txt"
    else:
        filename = sys.argv[2]
        nodes = parse(filename)
    print "Looking for %s" % start_node
    assert start_node in nodes

    result = dijkstra(nodes[start_node], set(nodes.values()))
    for node in result:
        print "{}: {}".format(node.name, node.cost)

    graphviz(filename.replace('.txt', '.dot'), nodes.values())
