import sys


class Node(object):
    def __init__(self, name, edges=None):
        self.name = name
        self.edges = edges if edges else set()
        self.cost = -1

    def __str__(self):
        return str(self.name)

class Edge(object):
    def __init__(self, src, cost, dst):
        self.src = src
        assert cost >= 0
        self.cost = cost
        self.dst = dst

    def __str__(self):
        return "{} -> {} {}".format(self.src, self.cost, self.dst)


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

def parse_edge(nodes, line):
    relation = line.split(' ')
    assert len(relation) == 4

    src = nodes.setdefault(relation[0], Node(relation[0]))
    nodes
    assert relation[1] == '->'
    cost = int(relation[2])
    dst = nodes.setdefault(relation[3], Node(relation[3]))
    edge = Edge(src, cost, dst)
    src.edges.add(edge)
    return edge


def parse(filename):
    nodes = {}
    for line in file(filename):
        edge = parse_edge(nodes, line.strip())
        #print edge
    return nodes


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
