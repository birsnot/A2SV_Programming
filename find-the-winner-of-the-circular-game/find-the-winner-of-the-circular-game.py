class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [i for i in range(n)]
        k -= 1
        n -= 1
        j = 0
        for _ in range(n):
            j += k
            j %= len(nums)
            nums.pop(j)
        return nums[0]+1
