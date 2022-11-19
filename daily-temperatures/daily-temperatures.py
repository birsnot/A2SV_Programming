class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                j = stack.pop()
                ans[j] = i-j
            stack.append(i)
        return ans
