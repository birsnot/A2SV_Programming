class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-n for n in stones]
        heapq.heapify(stones)
        n = 0
        while len(stones) > 1 or (len(stones) == 1 and n != 0):
            if n == 0:
                n1 = heapq.heappop(stones)
            else:
                n1 = heapq.heappushpop(stones, n)
            n2 = heapq.heappop(stones)
            n = n1-n2
        if stones:
            return -stones[0]
        else:
            return -n
