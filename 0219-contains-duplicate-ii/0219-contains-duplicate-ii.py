class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_set = set()
        N = len(nums)
        k = min(N, k + 1)
        for i in range(k):
            if nums[i] in num_set:
                return True
            num_set.add(nums[i])
        l = 0
        for i in range(k, N):
            num_set.remove(nums[l])
            if nums[i] in num_set:
                return True
            num_set.add(nums[i])
            l += 1
        return False