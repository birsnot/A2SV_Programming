class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.k_large = nums
        heapq.heapify(self.k_large)
        while len(self.k_large) > k:
            heapq.heappop(self.k_large)
            
    def add(self, val: int) -> int:
        if len(self.k_large) < self.k:
            heapq.heappush(self.k_large, val)
        else:
            heapq.heappushpop(self.k_large, val)
        return self.k_large[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
