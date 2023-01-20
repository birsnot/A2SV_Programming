class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ans = "".join(map(str, sorted(nums, key=self.getValue, reverse=True)))
        if ans[0] == "0":
            return "0"
        return ans
    
    def getValue(self, num):
        n = num
        prev = d = 0.9
        while n >= 10:
            n /= 10
            prev *= 10
            d += prev
        return num/d