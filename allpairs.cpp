#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <stdint.h>


using namespace std;

typedef uint64_t vertex_t;
typedef int64_t data_t;

typedef vector<vector<data_t>> graph_t;

ostream& operator<<(ostream& os, const graph_t& G) {

    for (auto row : G) {
        string delim = "";
        for (auto val : row) {
            os << delim << val;
            delim = ", ";
        }
        os << "\n";
    }
    return os;
}

graph_t init_matrix(size_t vertices, data_t init_value) {
    graph_t G(vertices);
    G.resize(vertices);
    for (auto i=0; i<vertices; ++i) {
        // cerr << "Setting size to 10000\n";
        G[i].resize(vertices);
        for (auto j=0; j<vertices; ++j) {
            if (i==j) {
                G[i][j] = 0;
            } else {
                G[i][j] = init_value;
            }
        }
    }
    return G;
}


// Returns the cheapest path in G
data_t floyd_warshall(graph_t& G) {
    graph_t current = init_matrix(G.size(), INT64_MAX);
    graph_t last = init_matrix(G.size(), INT64_MAX);

    for (auto i=0; i< G.size(); ++i) {
        for (auto j=0; j<G.size(); ++j) {
            if (i==j) {
                last[i][j] = 0;
            } else if (G[i][j] < INT64_MAX) {
                last[i][j] = G[i][j];
            }
        }

    }


    for (auto k=0; k<G.size(); ++k) {



        for(auto i=0; i<G.size(); ++i) {
            for (auto j=0; j<G.size(); ++j) {
                if (last[i][k] == INT64_MAX || last[k][j] == INT64_MAX) {
                    current[i][j] = last[i][j];
                } else {
                    current[i][j] = min(last[i][j],
                                        last[i][k] + last[k][j]);
                }
            }
        }
        //cerr << "last:\n" << last;
        //cerr << "current:\n" << current << "\n\n";
        swap(last, current);
        if (k > 0 && k % 100 == 0)
            cerr << "Finished iteration " << k << "/" << G.size() << "\n";
    }

    for (auto i=0; i<G.size(); ++i) {
        if (last[i][i] < 0) {
            cout << "error: found negative cycle in vertex " << i << endl;
            exit(-1);
        }
    }

    auto ret = INT64_MAX;
    for(auto i=0; i<G.size(); ++i) {
        for (auto j=0; j<G.size(); ++j) {
            ret = min(ret, last[i][j]);
        }
    }
    return ret;
}

pair<size_t,size_t> read_header(std::ifstream& f) {
    size_t vertices, edges;
    f >> vertices;
    f >> edges;
    return std::pair<size_t,size_t>(vertices,edges);
}

int main(int argc, char** argv) {
    if (argc < 2) {
        std::cerr << "Usage: allpairs <filename>\n";
        return -1;
    }

    auto filename = std::string(argv[1]);

    std::ifstream f(filename);

    auto header = read_header(f);
    auto vertices = header.first;
    auto edges = header.second;


    auto G = init_matrix(vertices, INT64_MAX);

    vertex_t tail, head;
    data_t cost;
    for (auto i = 0; i < edges; ++i) {
        f >> tail;
        f >> head;
        f >> cost;
        // cerr << "Setting G[" << tail << "," << head << "]: " << cost << "\n";
        G[tail-1][head-1] = cost;
    }
    cerr << "Created G of size " << G.size() << "x" << G[0].size() << "\n";

    auto min_cost = floyd_warshall(G);

    cout << min_cost << endl;
    return 0;
}
