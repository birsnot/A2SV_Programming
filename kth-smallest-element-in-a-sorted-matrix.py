class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        N = len(matrix)
        pq = []
        for i, row in enumerate(matrix):
            pq.append((-row.pop(), i))
        heapify(pq)
        k = N*N - k + 1
        while k:
            n, i = heappop(pq)
            if matrix[i]:
                heappush(pq, (-matrix[i].pop(), i))
            k -= 1
        return -n