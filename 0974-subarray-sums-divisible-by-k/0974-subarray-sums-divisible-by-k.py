class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sofar = {0: 1}
        sum_ = ans = 0
        for n in nums:
            sum_ += n
            check = sum_%k
            if check in sofar:
                ans += sofar[check]
                sofar[check] += 1
            else:
                sofar[check] = 1
        return ans