class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        for i in range(n-1):
            max_idx = i
            for j in range(i, n):
                if heights[j] > heights[max_idx]:
                    max_idx = j
            names[i], names[max_idx] = names[max_idx], names[i]
            heights[i], heights[max_idx] = heights[max_idx], heights[i]
        return names