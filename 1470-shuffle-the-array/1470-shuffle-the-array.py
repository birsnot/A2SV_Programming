class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l = 0
        r = n
        N = 2*n
        ans = [0]*(N)
        i = 0
        while r < N:
            ans[i] = nums[l]
            i += 1
            ans[i] = nums[r]
            i += 1
            l += 1
            r += 1
        return ans