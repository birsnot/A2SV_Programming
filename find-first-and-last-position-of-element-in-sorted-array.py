class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return (-1, -1)
        l = 0
        r = len(nums) - 1
        ans = [-1, -1]
        while l <= r:
            mid = l + (r - l)//2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if l >= len(nums) or nums[l] != target:
            return ans
        ans[0] = l
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l)//2
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        ans[1] = r
        return ans