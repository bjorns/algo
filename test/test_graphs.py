import unittest

from graphs import parse, Node, UndirectedEdge

class TestGraph(unittest.TestCase):
    def test_parse_undirected(self):
        g = parse('homework1/graphtest.txt', undirected=True)
        self.assertEqual(5, len(g.nodes))

        self.assertEqual('1', g.nodes['1'].name)
        self.assertEqual('2', g.nodes['2'].name)
        self.assertEqual('3', g.nodes['3'].name)

        self.assertEqual(2, len(g.nodes['1'].edges))
        self.assertEqual(3, len(g.nodes['2'].edges))
        self.assertEqual(2, len(g.nodes['3'].edges))

    def test_undirected_edge(self):
        v0 = Node("foo")
        v1 = Node("bar")

        edge = UndirectedEdge(v0, v1, 3)
        self.assertEqual(3, edge.cost)

        self.assertEqual(v0, edge.other_end(v1))
        self.assertEqual(v1, edge.other_end(v0))
