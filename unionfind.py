# coding=utf-8

class UnionFind(object):
    def __init__(self):
        self.leader = dict()
        self.followers = dict()

    def add(self, node, leader=None):
        if leader is None:
            leader = node

        self.leader[node] = leader
        self.followers.setdefault(leader, set()).add(node)

    def union(self, v0, v1):
        assert v0 == self.leader[v0]
        assert v1 == self.leader[v1]

        src = v1
        dst = v0

        for node in self.followers[src]:
            self.leader[node] = dst
            self.followers[dst].add(node)
        del self.followers[src]
        self.leader[src] = dst
        return dst

    def find(self, node):
        return self.leader[node]
