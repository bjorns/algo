import operator

def levies(data):
    left = 0
    ret = 0
    store = []
    for x in data:
        if left >= x > store[-1]:
            for i in range(len(store)):
                if store[-1-i] < x:
                    ret += x - store[-1-i]
                    store[-1-i] = x
                else:
                    break
        store.append(x)
        left = max(left, x)
    return ret


if __name__ == '__main__':
    x = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 4]
    print levies(x)
