class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """               
        if len(nums) == 3:
            if nums[0] + nums[2] == nums[1]*2:
                (nums[0], nums[1]) = (nums[1], nums[0])
            return nums
        incr = nums[1] - nums[0]
        i = 1
        while i < len(nums) - 2:
            if nums[i+1] - nums[i] == incr:
                (nums[i+1], nums[i+2]) = (nums[i+2], nums[i+1])
            incr = nums[i+1] - nums[i]
            i += 1

        if nums[-1] + nums[-3] == nums[-2]*2:
            if nums[-1] + nums[-2] != nums[0]*2:
                temp = nums[-1]
                nums[-1] = nums.pop(0)
                nums.append(temp)
            else:
                nums.insert(0, nums.pop())

        return nums
