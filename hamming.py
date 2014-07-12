# encoding: utf-8


def hamming_neighbours(x, dist=1, radix=24):
    ret = set()
    for i in range(radix):
        y = x ^ 2**i
        ret.add(y)
        if dist > 1:
            ret = ret | hamming_neighbours(y, dist-1, radix)
    return ret



total = set()
for i in range(200000):
    if i % 100 == 0:
        print i
    total = hamming_neighbours(i, 2)

print len(total)
