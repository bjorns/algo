import sys
from graphs import Graph, Node, Edge
import scc

def read_header(f):
    num_clauses = int(f.readline().strip())
    num_vars = num_clauses
    return num_clauses, num_vars

def create_edge(graph, src, dst):
    e = Edge(src, dst, 1)
    src.edges.add(e)
    dst.incoming_edges.add(e)
    graph.edges.add(e)

def make_graph(f):
    num_clauses, num_vars = read_header(f)
    g = Graph()
    print "\tCreating nodes."
    for x in range(1, num_clauses+1):
        g.add_node(Node(x))
        g.add_node(Node(-x))
    print "\tCreating edges."
    for _ in range(num_clauses):
        x0, x1 = map(int, f.readline().strip().split())
        create_edge(g, g.nodes[-x0], g.nodes[x1])
        create_edge(g, g.nodes[-x1], g.nodes[x0])
    return g

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "usage: ./homework2.py [1|2|3] <inputfile>"
        sys.exit(0)

    filename = sys.argv[1]
    f = open(filename, 'r')
    print "Creating graph."
    graph = make_graph(f)
    sccs = scc.run(graph, len(graph.nodes)/2)
    fail = False
    for component in sccs:
        for node in component:
            if node.name > 0:
                counternode = graph.nodes[-node.name]
                if counternode in component:
                    fail = True
                    print "Cannot satisfy x{} implies not x{}".format(node.name, node.name)
    if not fail:
        print "Satisfaction guaranteed."
