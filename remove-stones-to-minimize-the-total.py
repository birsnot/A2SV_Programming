class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        pq = [-n for n in piles]
        heapify(pq)
        for _ in range(k):
            n = heappop(pq)
            heappush(pq, n//2)
        return -sum(pq)