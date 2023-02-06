class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l = 0
        r = n
        N = 2*n
        ans = []
        while r < N:
            ans.append(nums[l])
            ans.append(nums[r])
            l += 1
            r += 1
        return ans