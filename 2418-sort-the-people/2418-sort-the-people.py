class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        names_ = []
        for i in sorted(range(n), key=lambda i: heights[i], reverse=True):
            names_.append(names[i])
        return names_