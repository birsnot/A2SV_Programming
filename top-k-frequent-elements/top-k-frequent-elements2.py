class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        return heapq.nlargest(k,c,key=lambda x: c[x])
