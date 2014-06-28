 # coding=utf-8

class Node(object):
    """ Vertex in graph. """

    def __init__(self, name):
        self.name = name
        self.edges = set()
        self.cost = -1

    def __str__(self):
        return self.name

class Edge(object):
    """ Edge between nodes."""

    def __init__(self, src, cost, dst):
        self.src = src
        assert cost >= 0
        self.cost = cost
        self.dst = dst

    def __str__(self):
        return "{} -> {} {}".format(self.src, self.cost, self.dst)


def _parse_line(line):
    relation = line.split(' ')
    assert len(relation) == 4
    src = relation[0]
    assert relation[1] == '->'
    cost = int(relation[2])
    dst = relation[3]
    return src, cost, dst


def parse(filename):
    """ Parse file into a mapping from name to Node object. """

    nodes = dict()
    for line in file(filename):
        src_name, cost, dst_name = _parse_line(line.strip())
        src = nodes.setdefault(src_name, Node(src_name))
        dst = nodes.setdefault(dst_name, Node(dst_name))
        edge = Edge(src, cost, dst)
        src.edges.add(edge)
    return nodes

def graphviz(filename, nodes):
    def label(node):
        return "\"{name} ({cost})\"".format(name=node.name, cost=node.cost)

    f = open(filename, 'w')
    f.write("digraph G {\n")
    for node in nodes:
        for edge in node.edges:
            f.write("\t{src} -> {dst}".format(src=label(edge.src), dst=label(edge.dst)))
            if edge.cost > 0:
                f.write("[label=\"{}\"]".format(edge.cost))
            f.write("\n")
    f.write("}\n")
