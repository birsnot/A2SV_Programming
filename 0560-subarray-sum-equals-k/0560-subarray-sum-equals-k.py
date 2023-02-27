class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        match = {0: 1}
        sum_ = ans = 0;
        for n in nums:
            sum_ += n
            ans += match.get(sum_ - k, 0)
            match[sum_] = match.get(sum_, 0) + 1
        return ans