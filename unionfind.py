# coding=utf-8

class UnionFind(object):
    def __init__(self):
        self.leader = dict()
        self.followers = dict()

    def add(self, node, leader):
        self.leader[node] = leader
        self.followers.setdefault(leader, set()).add(node)

    def union(self, v0, v1):
        src = v1
        dst = v0

        for node in self.followers[src]:
            self.leader[node] = dst
        del self.followers[src]
        return dst

    def find(self, node):
        return self.leader[node]
