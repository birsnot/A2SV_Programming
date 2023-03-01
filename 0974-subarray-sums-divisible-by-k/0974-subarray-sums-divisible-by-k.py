class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sofar = [0]*k
        sofar[0] = 1
        sum_ = ans = 0
        for n in nums:
            sum_ += n
            check = sum_%k
            ans += sofar[check]
            sofar[check] += 1
        return ans