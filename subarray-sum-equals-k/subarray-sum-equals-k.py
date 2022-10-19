class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        ans = 0
        match = {}
        for n in nums:
            temp = k+sum
            if temp in match:
                match[temp] += 1
            else:
                match[temp] = 1
            sum += n
            if sum in match:
                ans += match[sum]
        return ans
