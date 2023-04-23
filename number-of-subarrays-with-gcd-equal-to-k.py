class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans = 0
        start = -1
        for i in range(len(nums)):
            if nums[i] % k != 0:
                start = i
            else:
                d = nums[i]
                j = i-1
                while j>start and d!=k:
                    d = gcd(d, nums[j])
                    j -= 1
                if d==k:  ans += j-start+1
        return ans