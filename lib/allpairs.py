# encoding: utf-8
import sys


def init_matrix(G, i,j,k):
    if i == j:
        return 0
    elif i<len(G) and j<len(G) and G[i][j]:
        return G[i][j]
    else:
        return sys.maxint


def floyd_warshall(G):
    assert len(G) == len(G[0])

    n = len(G)
    A = [[[init_matrix(G, i,j,k) for k in range(n+1)] for j in range(n+1)] for i in range(n+1)]


    for k in range(1,n+1):
        print "Iteration {}/{}".format(k, n+1)
        for i in range(1,n+1):
            for j in range(1,n+1):
                A[i][j][k] = min(A[i][j][k-1],
                                 A[i][k][k-1] + A[k][j][k-1])
    return A
