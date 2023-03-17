class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        N = len(nums)
        temp = []
        def subset(i):
            if i == N:
                ans.append(temp.copy())
                return
            temp.append(nums[i])
            subset(i + 1)
            temp.pop()
            subset(i + 1)
        subset(0)
        return ans