# coding=utf-8

class UnionFind(object):
    def __init__(self):
        self.leader = dict()
        self.followers = dict()
        self.clusters = 0

    def add(self, node):
        assert node not in self.leader
        assert node not in self.followers

        self.leader[node] = node
        self.followers.setdefault(node, set())
        self.clusters += 1

    def union(self, v0, v1):
        v0 = self.leader[v0]
        v1 = self.leader[v1]
        if v0 == v1:
            return

        f0 = len(self.followers[v0])
        f1 = len(self.followers[v1])

        src = v0 if min(f0,f1) == f0 else v1
        dst = v1 if src == v0 else v0

        for node in self.followers[src]:
            self.leader[node] = dst
            self.followers[dst].add(node)
        del self.followers[src]
        self.leader[src] = dst
        self.clusters -= 1
        return dst

    def find(self, node):
        return self.leader[node]
