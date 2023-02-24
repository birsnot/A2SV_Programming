class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_set = set()
        k += 1
        for n in nums[:k]:
            if n in num_set:
                return True
            num_set.add(n)
        l = 0
        for n in nums[k:]:
            num_set.remove(nums[l])
            if n in num_set:
                return True
            num_set.add(n)
            l += 1
        return False