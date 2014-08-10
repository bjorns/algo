""" Calculate strongly connected components. """


def get_scc(node, start, scc):
    stack = [node]
    while len(stack) > 0:
        node = stack.pop()
        node.leader = start
        scc.add(node)
        for e in node.edges:
            if not hasattr(e.dst, 'leader'):
                stack.append(e.dst)
    return scc


def set_finish_time(node, t, finish_times):
    stack = []
    stack.append(node)
    while len(stack) > 0:
        node = stack.pop()
        for e in node.incoming_edges:
            if not hasattr(e.src, 'finish_time'):
                stack.append(e.src)
        t += 1
        node.finish_time = t
        finish_times[t] = node
    return t

def first_pass(graph, i, t, finish_times):

    node = graph.nodes[i]
    if not hasattr(node, 'finish_time'):
        t = set_finish_time(node, t, finish_times)
    return t

def run(graph, n):
    t = 0
    finish_times = dict()
    print "Running first pass scc  to {}".format(n)
    for i in reversed(range(1, n+1)):
        t = first_pass(graph, i, t, finish_times)
    for i in range(1, n+1):
        t = first_pass(graph, -i, t, finish_times)
    print "Top finish time is {}".format(t)
    print "Running second pass scc."
    sccs = []
    for i in reversed(range(1, 2*n+1)):
        node = finish_times[i]
        if not hasattr(node, 'leader'):
            node.leader = node
            scc = get_scc(node, node, set())
            sccs.append(scc)
    return sccs
