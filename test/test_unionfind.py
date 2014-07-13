import unittest

from unionfind import UnionFind
from graphs import Node

class TestUnionFind(unittest.TestCase):
    def test_setup(self):
        u = UnionFind()
        self.assertEqual(dict(), u.leader)
        self.assertEqual(dict(), u.followers)

    def test_add_node(self):
        u = UnionFind()
        foo = Node("foo")
        bar = Node("bar")
        baz = Node("baz")
        u.add(foo)
        u.add(bar)
        u.add(baz)
        self.assertEqual(3, len(u.leader))
        self.assertEqual(foo, u.leader[foo])
        self.assertEqual(bar, u.leader[bar])
        self.assertEqual(baz, u.leader[baz])

        self.assertEqual(3, len(u.followers))
        self.assertEqual(set(), u.followers[foo])
        self.assertEqual(set(), u.followers[bar])
        self.assertEqual(set(), u.followers[baz])

    def test_find(self):
        u = UnionFind()
        foo = Node("foo")
        u.add(foo)
        self.assertEqual(foo, u.find(foo))

    def test_union(self):
        u = UnionFind()
        foo = Node("foo")
        u.add(foo)

        bar = Node("bar")
        u.add(bar)

        self.assertEqual(foo, u.find(foo))
        self.assertEqual(bar, u.find(bar))

        u.union(foo, bar)

        self.assertEqual(bar, u.find(foo))
        self.assertEqual(bar, u.find(bar))
