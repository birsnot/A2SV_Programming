class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ans = deque()
        for n in nums:
            if n%2 == 0:
                ans.appendleft(n)
            else:
                ans.append(n)
        return ans