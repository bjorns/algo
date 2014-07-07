import unittest

from unionfind import UnionFind
from graphs import Node

class TestGraph(unittest.TestCase):
    def test_setup(self):
        u = UnionFind()
        self.assertEqual(dict(), u.leader)
        self.assertEqual(dict(), u.followers)

    def test_add_node(self):
        u = UnionFind()
        leader = Node("leader")
        foo = Node("foo")
        bar = Node("bar")
        baz = Node("baz")
        u.add(foo, leader)
        u.add(bar, leader)
        u.add(baz, leader)
        self.assertEqual(3, len(u.leader))
        self.assertEqual(leader, u.leader[foo])
        self.assertEqual(leader, u.leader[bar])
        self.assertEqual(leader, u.leader[baz])

        self.assertEqual(1, len(u.followers))
        self.assertEqual({foo, bar, baz}, u.followers[leader])

    def test_find(self):
        u = UnionFind()
        leader = Node("leader")
        foo = Node("foo")
        u.add(foo, leader)
        self.assertEqual(leader, u.find(foo))

    def test_union(self):
        u = UnionFind()
        leader0 = Node("leader0")
        foo = Node("foo")
        u.add(foo, leader0)


        leader1 = Node("leader0")
        bar = Node("bar")
        u.add(bar, leader1)

        self.assertEqual(leader0, u.find(foo))
        self.assertEqual(leader1, u.find(bar))

        u.union(leader0, leader1)

        self.assertEqual(leader0, u.find(foo))
        self.assertEqual(leader0, u.find(bar))
