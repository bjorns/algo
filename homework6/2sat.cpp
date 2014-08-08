#include <cassert>
#include <cmath>
#include <ctime>
#include <cstdlib>

#include <fstream>
#include <iostream>
#include <iterator>
#include <map>
#include <string>
#include <utility>
#include <vector>
#include <set>

using namespace std;

static const bool DEBUG=false;


typedef pair<int,int> header_t;

struct clause_t {
    int x0, x1;
    bool val0, val1;
};

ostream& operator<<(ostream& os, const clause_t& clause) {
    if (!clause.val0)
        os << "!";
    os << "x" << clause.x0 + 1 << " | ";
    if (!clause.val1)
        os << "!";
    os << "x" << clause.x1 + 1;
    return os;
}

ostream& operator<<(ostream& os, const vector<bool>& vars) {
    for (auto i=0; i < vars.size(); ++i) {
        os << "x" << i+1 << "=" << vars[i] << "\n";
    }
    return os;
}

ostream& operator<<(ostream& os, const set<int>& clauses) {
    for (auto& clause : clauses) {
        os << clause << "\n";
    }
    return os;
}

void init_vars(vector<bool>& vars) {
    srand(time(0));
    for (int i=0; i<vars.size(); ++i) {
        int x = rand();
        vars[i] = x % 2;
    }
}

bool check_clause(const clause_t& clause, const vector<bool>& vars) {
    return vars[clause.x0] == clause.val0 || vars[clause.x1] == clause.val1;
}

set<int> init_failing_clauses(const vector<bool>& vars, const vector<clause_t>& clauses) {
    set<int> ret;
    for (int c=0; c < clauses.size(); ++c) {
        auto sat = check_clause(clauses[c], vars);
        if (!sat) {
            ret.insert(c);
        }
    }
    return ret;
}

bool papadimitrious(vector<bool>& vars, const vector<clause_t>& clauses, const vector<vector<int>>& related_clauses) {


    const int n = vars.size();
    for(int i=0; i < n/1000; ++i) {
        vector<int> switches;
        switches.resize(vars.size());


        init_vars(vars);

        if (DEBUG)
            cerr << "New draft " << i << "\n";
        cerr << ".";
        auto&& failing_clauses = init_failing_clauses(vars, clauses);
        if (DEBUG) {
            cerr << "Failing clauses are:\n";
            for (auto c : failing_clauses) {
                cerr << clauses[c] << "\n";
            }
            cerr << "\n\n";
        }

        for (uint64_t j=0; j < n*n/100; ++j) {
            if (failing_clauses.empty()) {
                return true;
            } else {

                auto it = failing_clauses.begin();

                auto c0 = *it;
                auto clause_to_fix = clauses[c0];


                bool switch_x0 = rand() % 2;
                auto v = switches[clause_to_fix.x0] > switches[clause_to_fix.x1] ? clause_to_fix.x1 : clause_to_fix.x0;
                switches[v]++;
                if (DEBUG)
                    cerr << "Running another switch of x" << v+1 << ".\n";
                vars[v] = !vars[v];
                failing_clauses.erase(c0);


                const vector<int>& related = related_clauses[v];
                for (auto c1 : related) {
                    if (check_clause(clauses[c1], vars)) {
                        failing_clauses.erase(c1);
                    } else {
                        failing_clauses.insert(c1);
                    }
                }

                if (DEBUG) {
                    cerr << "Failing clauses are:\n";
                    for (auto _c : failing_clauses) {
                        cerr << clauses[_c] << "\n";
                    }
                    cerr << "\n\n";
                }

            }
        }
    }
    return false;
}


// Map a variable to all clauses that are affected by it.
vector<vector<int>> map_vars_to_clauses(int num_vars, const vector<clause_t>& clauses) {
    vector<vector<int>> ret;
    ret.resize(num_vars);
    for (int c=0; c < clauses.size(); ++c) {
        auto clause = clauses[c];
        ret[clause.x0].push_back(c);
        ret[clause.x1].push_back(c);
    }
    return ret;
}

header_t read_header(ifstream& f) {
    int num_vars;
    f >> num_vars;
    int num_clauses = num_vars;
    return pair<int,int>(num_vars, num_clauses);
}

vector<clause_t> read_clauses(ifstream& f, int num_clauses) {
    vector<clause_t> ret;
    ret.resize(num_clauses);
    int x0,x1;
    for(int i=0; i<num_clauses; ++i) {
        f >> x0;
        f >> x1;
        clause_t clause;
        assert(x0!=0);
        assert(x1!=0);
        clause.x0 = abs(x0) - 1;
        clause.val0 = x0 >= 0;
        clause.x1 = abs(x1) - 1;
        clause.val1 = x1 >= 0;
        ret[i] = clause;
    }
    return ret;
}

int main(int argc, char** argv) {
    if (argc < 2) {
        cerr << "Usage: 2sat <filename>\n";
        return -1;
    }

    auto filename = std::string(argv[1]);
    cerr << "reading header from " << filename << "\n";
    std::ifstream f(filename);

    auto header = read_header(f);
    auto num_vars = header.first;
    auto num_clauses = header.second;

    cerr << "Working with " << num_vars << " variables and " << num_clauses << " clauses.\n";

    const vector<clause_t>&& clauses = read_clauses(f, num_clauses);

    auto&& related_clauses = map_vars_to_clauses(num_vars, clauses);
    if (DEBUG) {
        for (int i=0; i < related_clauses.size(); ++i) {
            cerr << "x" << i+1 << ":\n";
            for (int j=0; j < related_clauses[i].size(); ++j) {
                cerr << "\t" << clauses[related_clauses[i][j]] << "\n";
            }
        }
    }

    vector<bool> vars;
    vars.resize(num_vars);
    auto success = papadimitrious(vars, clauses, related_clauses);

    if (success) {
        for (const clause_t& clause : clauses) {
            if (!check_clause(clause, vars)) {
                cerr << "Failed to verify clause " << clause << "\n";
            }
        }
        cout << "Success.\n";
        // cout << vars << "\n";
    } else {
        cerr << "Can't get no satisfaction.\n";
        return -1;
    }
}
