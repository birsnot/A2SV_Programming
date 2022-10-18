class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = z = ans = j = i = 0
        while i < len(nums):
            count += 1
            if nums[i] == 0:
                z += 1
                if z > k:
                    while True:
                        count -= 1
                        if nums[j] == 0:
                            z -= 1
                            j += 1
                            break
                        j += 1
            i += 1
            ans = max(ans, count)
        return ans
