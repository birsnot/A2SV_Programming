class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            count = 0
            mask = 1<<i
            for n in nums:
                if n&mask:
                    count += 1
            if count%3:
                ans |= mask
        if ans >= 1<<31:
            return ans - (1<<32)
        return ans