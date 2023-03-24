class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        nums_ = []
        prev = set()
        for n in nums:
            if n not in prev:
                nums_.append(n)
                prev.add(n)
            else:
                nums_.append(-101)
        ans = []
        N = len(nums)
        temp = []
        def helper(i):
            for j in range(i, N):
                if not temp:
                    if nums_[j] != -101:
                        temp.append(nums[j])
                        helper(j + 1)
                        temp.pop()
                elif temp[-1] <= nums[j]:
                    if nums_[j] != -101:
                        temp.append(nums[j])
                        ans.append(temp.copy())
                        helper(j + 1)
                        temp.pop()
                    else:
                        temp.append(nums[j])
                        if temp not in ans:
                            ans.append(temp.copy())
                            helper(j + 1)
                        temp.pop()
        helper(0)
        return ans