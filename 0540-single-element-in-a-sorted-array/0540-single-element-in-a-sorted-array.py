class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        N = len(nums) - 1
        left = 0
        right = N//2
        mid = left + right
        while mid < N:
            mid -= mid%2
            if nums[mid] != nums[mid+1]:
                if mid == 0 or nums[mid] != nums[mid-1]:
                    return nums[mid]
                right = mid//2 - 1
            else:
                left = mid//2 + 1
            mid = left + right
        return nums[N]