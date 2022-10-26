class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def helper(nums):
            if len(nums) == 1:
                return nums[0], 0
            if len(nums) == 2:
                if nums[0] > nums[1]:
                    return nums[0], nums[1]
                else:
                    return nums[1], nums[0]
            c1 = helper(nums[1:-1])
            c2 = helper(nums[2:])
            c3 = helper(nums[:-2])
            d1 = c1[0]-c1[1]
            dl = d1 + nums[0]-nums[-1]
            dr = d1 + nums[-1]-nums[0]
            dll = c2[0]-c2[1] + nums[0]-nums[1]
            drr = c3[0]-c3[1] + nums[-1]-nums[-2]
            left = min(dl, dll)
            right = min(dr, drr)
            return max(left, right), 0

        p1, p2 = helper(nums)
        if p2 > p1:
            return False
        else:
            return True
