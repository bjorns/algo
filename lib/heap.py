import heapq

def delete_nth(heap, n):
    heap[n] = heap[-1]
    heap.pop()
    if n < len(heap) - 1:
        heapq._siftup(heap, n)
