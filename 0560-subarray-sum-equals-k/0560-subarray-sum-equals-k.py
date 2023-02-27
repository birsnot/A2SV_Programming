class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        match = defaultdict(int)
        match[0] += 1
        ans = sum_ = 0
        for n in nums:
            sum_ += n
            ans += match[sum_ - k]
            match[sum_] += 1
        return ans