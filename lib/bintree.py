import sys

def solve(items):
    n = len(items)
    A = [[0 for _ in range(n)] for _ in range(n)]

    for s in range(n):
        print "Running iteration {}".format(s)
        for i in range(n):
            j = min(i+s, n-1)
            print "i: {} j: {}".format(i, j)
            _min = sys.maxint
            K = sum_p(items, i, j)
            print "K: {}".format(K)
            for r in range(i,j+1):
                A1 = A[i][r-1] if i <= r-1 else 0
                A2 = A[r+1][j] if r+1 <= j else 0
                x = K + A1 + A2
                _min = min(x, _min)
            A[i][j] = _min
    print A
    return A[0][n-1]

def sum_p(items, i, j):
    ret = 0
    for x in range(i, j+1):
        name, freq = items[x]
        print "Adding items[{}]: {}".format(x, freq)
        ret += freq
    return ret

def parse(f):
    num_items = _parse_header(f)
    print "Items: {}".format(num_items)

    items = []
    for i in range(num_items):
        value, frequency = _num(f.readline().strip().split(' '))
        items.append((value, frequency))
    return items

def _num(vec):
    return vec[0], float(vec[1])

def _parse_header(f):
    return int(f.readline().strip())
