import sys
import heapq

def get_entry(f):
    line = f.readline().strip()
    left, right = line.split(' ')
    weight, length = (int(left), int(right))
    return (-weight + length, -weight, -length)

def weighted_sum(filename):
    f = open(filename, 'r')
    num_lines = int(f.readline())
    x = [get_entry(f) for _ in range(num_lines)]

    heapq.heapify(x)
    t = 0
    S = 0
    for _ in range(num_lines):
        entry = heapq.heappop(x)
        print entry
        diff,weight,length = entry
        weight = -weight
        length = -length
        t = t + length
        S = S + weight * t
    print S


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "usage: ./homework1.py [1|2|3] <inputfile>"
        sys.exit(0)
    question = sys.argv[1]
    if question == '1':
        filename = sys.argv[2]
        weighted_sum(filename)
    else:
        print 'Unknown assignment: ' + question
