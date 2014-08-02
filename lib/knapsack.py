# encoding: utf-8
import time

def key(i,x):
    return i << 32 | x

def A(items, i, x, cache=None):
    if x <= 0:
        return 0
    if i <= 0:
        return 0

    if not cache:
        cache = dict()
    cached_value = cache.get(key(i,x))

    if cached_value:
        return cached_value

    v_i,w_i = items[i-1]
    if w_i > x:
        return A(items, i-1, x, cache)
    else:
        return max(A(items, i-1, x, cache),
                   A(items, i-1, x - w_i, cache) + v_i)


def solve_recursive(items, capacity):
    return A(items, len(items), capacity)

def solve(items, capacity):
    n = len(items)

    current = [0 for _ in range(capacity+1)]
    last    = [0 for _ in range(capacity+1)]
    for i in range(1, n+1):
        v_i,w_i = items[i-1]
        for x in range(capacity+1):
            if w_i > x:
                current[x] = last[x]
            else:
                current[x] = max(last[x],
                                 last[x - w_i] + v_i)

        last,current = current,last
        print "finished iteration {}/{}".format(i,n)
    return last[-1]


##
## Parser
def _parse_header(f):
    x, y = f.readline().strip().split(' ')
    return int(x), int(y)

def _int(x):
    return int(x[0]), int(x[1])

def parse(f):
    (capacity, num_items) = _parse_header(f)
    print "Capacity: {}".format(capacity)
    print "Items: {}".format(num_items)

    items = []
    for i in range(num_items):
        value, weight = _int(f.readline().strip().split(' '))
        items.append((value,weight))
    return items, capacity
