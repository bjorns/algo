#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <stdint.h>

using namespace std;

typedef std::pair<uint64_t,uint64_t> entry;

uint64_t solve(vector<entry>& items, uint64_t capacity) {
    std::vector<uint64_t> *current_line = new std::vector<uint64_t>(capacity+1);
    std::vector<uint64_t> *last_line = new std::vector<uint64_t>(capacity+1);

    auto n = items.size();
    for (int i = 1; i < n+1; ++i) {
        entry item = items[i-1];
        auto v_i = item.first;
        auto w_i = item.second;

        for (int x = 0; x < capacity+1; ++x) {
            if (w_i > x) {
                (*current_line)[x] = (*last_line)[x];
            } else {
                (*current_line)[x] = std::max((*last_line)[x],
                                              (*last_line)[x - w_i] + v_i);
            }
        }
        auto tmp = current_line;
        current_line = last_line;
        last_line = tmp;
    }
    return (*last_line)[capacity];
}

pair<uint64_t,uint64_t> read_header(std::ifstream& f) {
    uint64_t lines, capacity;
    f >> capacity;
    
    f >> lines;
    return std::pair<uint64_t,uint64_t>(capacity,lines);
}

int main(int argc, char** argv) {
    if (argc < 2) {
        std::cerr << "Usage: knapsack <filename>\n";
        return -1;
    }

    auto filename = std::string(argv[1]);

    std::ifstream f(filename);

    auto header = read_header(f);
    auto capacity = header.first;
    auto num_lines = header.second;



    std::vector<entry> data(num_lines);

    uint64_t value, weight;
    for (auto i = 0; i < num_lines; ++i) {
        f >> value;
        f >> weight;
        data[i] = entry(value, weight);
    }
    auto cost = solve(data, capacity);
    cout << cost << endl;
    return 0;
}
