 # coding=utf-8
import random
from datetime import datetime

random.seed(datetime.now())

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


def generate_nodes(size, nodenames):
    nodes = dict()
    size = min(size, len(nodenames))
    print "Generating graph of size %s" % size
    for i in range(size):
        node = Node(nodenames[i])
        nodes[node.name] = node
    return nodes


def generate_edges(graph, nodenames):
    size = len(graph)
    for src in graph.values():
        for i in range(random.randint(1, 2)):
            j = random.randint(0, size-1)
            dst_name = nodenames[j]
            dst = graph[dst_name]
            cost = random.randint(1, 20)
            edge = Edge(src, cost, dst)
            src.edges.add(edge)

def generate(size, nodenames):
    graph = generate_nodes(size, nodenames)
    generate_edges(graph, nodenames)
    return graph


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
            if edge.src.cost >= 0 and edge.dst.cost >= 0:
                f.write("\t{src} -> {dst}".format(src=label(edge.src), dst=label(edge.dst)))
                if edge.cost > 0:
                    f.write("[label=\"{}\"]".format(edge.cost))
                f.write("\n")
    f.write("}\n")
