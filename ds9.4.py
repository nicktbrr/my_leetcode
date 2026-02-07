import heapq


def k_smallest(matrix, k):
    res = []
    res = res + [el for el in elements]
    heap = []
    for r in len(matrix):
        for c in len(matrix[0]):
            heapq.heappush(heap, matrix[r][c])
    for _ in range(k - 1):
        heapq.heappop()
    return heapq.heappop()
