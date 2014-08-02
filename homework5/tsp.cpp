#include <algorithm>
#include <cassert>
#include <cmath>
#include <fstream>
#include <iostream>
#include <limits>
#include <utility>
#include <stdint.h>
#include <string>
#include <vector>

using namespace std;

typedef pair<float,float> point_t;
struct entry {
    point_t pos;
    int id;

    entry() : id(-1) {};
    entry(const int& id);
    entry(const float& x, const float& y, const int& id);
};
typedef vector<vector<float>> matrix_t;

entry::entry(const int& id)
    : pos(point_t(0,0)), id(id)
{}

entry::entry(const float& x, const float& y, const int& id)
    : pos(point_t(x,y)), id(id)
{}

bool operator==(const entry& lval,  const entry& rval) {
    return lval.id == rval.id;
}

bool operator<(const entry& lval,  const entry& rval) {
    return lval.id < rval.id;
}

ostream& operator<<(ostream& os, const entry& e) {
    os << e.id << " (" << e.pos.first<< ","<<e.pos.second << ")";
    return os;
}

ostream& operator<<(ostream& os, const matrix_t& A) {
    for (auto row : A) {
        string delim = "";
        for (auto val : row) {
            os << delim << val;
            delim = ",\t";
        }
        os << "\n";
    }
    return os;
}

int read_header(ifstream& f) {
    int points;
    f >> points;
    return points;
}

entry read_entry(ifstream& f, int i) {
    float x,y;
    f >> x;
    f >> y;
    entry e(x,y, i);
    return e;
}

vector<entry> read_cities(ifstream& f, int size) {
    vector<entry> ret(size+1);
    ret.resize(size+1);
    entry start;
    for (auto i = 1; i <= size; ++i) {
        entry e = read_entry(f, i);
        if (i == 0) {
            start = e;
            cerr << "Start is " << start << "\n";
        }
        ret[i] = e;
    }
    return ret;
}

matrix_t init_matrix(int problem_size) {
    matrix_t A;
    int num_permutations = (1<<problem_size);

    A.resize(num_permutations);
    for (int i=0; i < num_permutations; ++i) {
        A[i].resize(problem_size+1);
        for (int j=0; j <= problem_size; ++j) {
            A[i][j] = (i==1) ? 0 : std::numeric_limits<float>::max() / 2;
        }
    }
    return A;
}

uint64_t encode(int id) {
    return (1<<(id-1));
}

float distance(const entry& x0, const entry& x1) {
    auto w = x1.pos.first - x0.pos.first;
    auto h = x1.pos.second - x0.pos.second;
    return sqrt(w*w + h*h);
}

void permute(int n, int m, int depth, int index, int* buffer, matrix_t& A,
             const vector<entry>& cities) {
    if (depth > m-1) {
        uint64_t num = 0;
        for (int x=0; x<m; x++) {
            auto j = buffer[x];
            // cerr << j << " ";
            num = num | encode(j);
        }
        // cerr << ": " << num << "\n";

        for (int x=0; x<m; x++) {
            auto j = buffer[x];
            // cerr << "j: " << j << "\n";
            float mincost = std::numeric_limits<float>::max()/2;
            for(int y=0; y<m; ++y) {
                auto k = buffer[y];
                // cerr << "k: " << k << "\n";
                if (k != j) {
                    auto num2 = num & (~encode(j));
                    auto d_kj = distance(cities[k], cities[j]);
                    //cerr << "Distance " << cities[k] << " and " << cities[j] << " is " << d_kj << "\n";

                    mincost = min(A[num2][k] + d_kj, mincost);
                    //cerr << "Setting mincost to " <<  mincost << " via " << A[num2][k] << " and " << d_kj << "\n";
                }
            }
            A[num][j] = mincost;
        }
    } else {
        // Remember to skip if not S -> {1}
        for (int p=index; p < n-m+1 + depth; p++) {
            buffer[depth] = p+1;
            permute(n, m, depth+1, p+1, buffer, A, cities);
        }
    }
}

int main(int argc, char** argv) {
    if (argc < 2) {
        cerr << "Usage: tsp <filename>\n";
        return -1;
    }

    auto filename = std::string(argv[1]);
    cerr << "reading header from " << filename << "\n";
    std::ifstream f(filename);

    auto num_cities = read_header(f);
    cerr << "Working with " << num_cities << " cities.\n";

    vector<entry> cities = read_cities(f, num_cities);

    cerr << "Initializing matrix.\n";
    matrix_t A = init_matrix(num_cities);

    int buffer[128];
    cerr << "Running algorithm.\n";
    for (int m=2; m <= num_cities; ++m) { // subproblem size
        cerr << "Analyzing problem size " << m << "\n";
        permute(num_cities, m, 0, 0, buffer, A, cities);
    }
    //cout << A << "\n";

    cerr << "Calculating result.\n";
    float mincost = std::numeric_limits<float>::max()/2;
    for (int j=2; j <= num_cities; ++j) {
        auto S = (1<<num_cities)-1;
        mincost = min(mincost, A[S][j] + distance(cities[j], cities[1]));
    }
    cout << "Result: " << mincost << "\n";
}
