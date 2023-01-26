class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        ans = 0
        while left < right:
            min_h = min(height[left], height[right])
            ans = max(ans, min_h*(right-left))
            if height[left] < height[right]:
                while height[left] <= min_h:
                    left += 1
            else:
                right -= 1
                while height[right] < min_h:
                    right -= 1
        return ans