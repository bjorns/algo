import unittest

import graph

class TestGraph(unittest.TestCase):
    def test_parse_undirected(self):
        g = graph.parse('homework1/graphtest.txt', undirected=True)
        self.assertEqual(5, len(g))

        self.assertEqual('1', g['1'].name)
        self.assertEqual('2', g['2'].name)
        self.assertEqual('3', g['3'].name)

        self.assertEqual(2, len(g['1'].edges))
        self.assertEqual(3, len(g['2'].edges))
        self.assertEqual(2, len(g['3'].edges))

    def test_undirected_edge(self):
        v0 = graph.Node("foo")
        v1 = graph.Node("bar")

        edge = graph.UndirectedEdge(v0, v1, 3)
        self.assertEqual(3, edge.cost)

        self.assertEqual(v0, edge.other_end(v1))
        self.assertEqual(v1, edge.other_end(v0))
