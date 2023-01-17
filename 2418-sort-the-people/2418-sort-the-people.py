class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        for last_i in range(n-1, 0, -1):
            swap = False
            for i in range(last_i):
                i2 = i + 1
                if heights[i] < heights[i2]:
                    heights[i], heights[i2] = heights[i2], heights[i]
                    names[i], names[i2] = names[i2], names[i]
                    swap = True
            if not swap:
                break
        return names