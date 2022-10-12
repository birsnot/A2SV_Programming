class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0,0,0]
        for n in nums:
            colors[n] += 1
        nums.clear()
        for color in range(3):
            for _ in  range(colors[color]):
                nums.append(color)
