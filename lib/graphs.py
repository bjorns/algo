# coding=utf-8
import random
from datetime import datetime

random.seed(datetime.now())

class Graph(object):
    """ A Adjecency list implementation of a graph. """
    def __init__(self):
        self.nodes = dict()
        self.edges = set()

    def add_node(self, node):
        assert node.name not in self.nodes
        self.nodes[node.name] = node

    def get_nodes(self):
        return set(self.nodes.values())

    def random_node(self):
        name = random.sample(self.nodes, 1)[0]
        return self.nodes[name]

class Node(object):
    """ Vertex in graph. """

    def __init__(self, name):
        self.name = name
        self.edges = set()
        self.cost = -1

    def __str__(self):
        return self.name


class Edge(object):
    """ Directed Edge between nodes."""

    def __init__(self, src, dst, cost):
        self.src = src
        assert cost >= 0
        self.cost = cost
        self.dst = dst

    def __str__(self):
        return "{} -> {} {}".format(self.src, self.cost, self.dst)


class UndirectedEdge(object):
    """ Undirected Edge between nodes."""

    def __init__(self, v0, v1, cost):
        self.v0 = v0
        self.v1 = v1
        self.cost = cost
        self.spanning = False

    def other_end(self, node):
        return self.v1 if node == self.v0 else self.v0

    def __str__(self):
        return "{} {} {}".format(self.v0, self.v1, self.cost)


def generate_nodes(size, nodenames):
    nodes = dict()
    size = min(size, len(nodenames))
    for i in range(size):
        node = Node(nodenames[i])
        nodes[node.name] = node
    return nodes


def generate_edges(graph, nodenames, undirected=False):
    size = len(graph)
    for src in graph.values():
        for i in range(random.randint(1, 2)):
            j = random.randint(0, size-1)
            dst = graph[nodenames[j]]
            cost = random.randint(1, 20)
            edge = Edge(src, cost, dst)
            src.edges.add(edge)
            if undirected:
                edge = Edge(dst, cost, src)
                dst.edges.add(edge)


def generate(size, nodenames, undirected=False):
    graph = generate_nodes(size, nodenames)
    generate_edges(graph, nodenames, undirected)
    return graph


def _parse_line(line):
    relation = line.split(' ')
    assert len(relation) == 3
    v0 = int(relation[0])
    v1 = int(relation[1])
    cost = int(relation[2])
    return v0, v1, cost


def _get_node(graph, name):
    if name in graph.nodes:
        return graph.nodes[name]
    else:
        node = Node(name)
        graph.add_node(node)
        return node


def read_header(f):
    line = f.readline().strip().split(' ')
    if len(line) == 2:
        x,y = line
        nodes, edges = int(x), int(y)
    elif len(line) == 1:
        nodes = int(line[0])
        edges = (nodes**2 - nodes) / 2
    return nodes, edges

def parse(filename, undirected=False):
    """ Parse file into a mapping from name to Node object. """
    graph = Graph()

    f = open(filename, 'r')
    num_nodes, num_edges = read_header(f)
    for _ in range(num_edges):
        line = f.readline().strip()
        v0_name, v1_name, cost = _parse_line(line.strip())
        v0 = _get_node(graph, v0_name)
        v1 = _get_node(graph, v1_name)
        if undirected:
            edge = UndirectedEdge(v0, v1, cost)
            v0.edges.add(edge)
            v1.edges.add(edge)
        else:
            edge = Edge(v0, v1, cost)
            v0.edges.add(edge)
        graph.edges.add(edge)
    return graph


def parse_matrix(f):
    num_nodes, num_edges = read_header(f)
    print num_nodes
    G = [[None for _ in range(num_nodes)] for _ in range(num_nodes)]
    for _ in range(num_edges):
        line = f.readline().strip()
        v0, v1, cost = _parse_line(line.strip())
        G[v0-1][v1-1] = cost
    return G


def label(node):
    if node.cost >= 0:
        return "\"{name} ({cost})\"".format(name=node.name, cost=node.cost)
    else:
        return "\"{name}\"".format(name=node.name)

def dot_format(f, nodes):
    f.write("digraph G {\n")
    for node in nodes:
        for edge in node.edges:
            if edge.src.cost >= 0 and edge.dst.cost >= 0:
                f.write("\t{src} -> {dst}".format(src=label(edge.src), dst=label(edge.dst)))
                if edge.cost > 0:
                    f.write("[label=\"{}\"]".format(edge.cost))
                f.write("\n")
    f.write("}\n")

def neato_format(f, edges):
    f.write("graph G {\n")

    for edge in edges:
        f.write("\t{src} -- {dst}".format(src=label(edge.v0), dst=label(edge.v1)))
        f.write("[label=\"{}\"]".format(edge.cost))
        f.write("\n")
        if edge.spanning:
            f.write("\t{src} -- {dst}".format(src=label(edge.v0), dst=label(edge.v1)))
            f.write("[color=\"red\"]")
            f.write("\n")

    f.write("}\n")


def graphviz(filename, edges, undirected=False):
    f = open(filename, 'w')
    if undirected:
        dot_format(f, edges)
    else:
        neato_format(f, edges)
    f.close()
