class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N = len(nums)
        for i in range(N):
            while nums[i] != i + 1:
                j = nums[i] - 1
                if nums[j] == -1:
                    nums[j], nums[i] = nums[i], nums[j]
                    break
                elif nums[j] != nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]
                else:
                    nums[i] = -1
                    break
        ans = []
        for i in range(N):
            if nums[i] == -1:
                ans.append(i + 1)
        return ans