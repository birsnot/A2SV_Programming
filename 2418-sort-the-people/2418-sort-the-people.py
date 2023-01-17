class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        names_ = [""]*n
        sorted_idx = sorted(range(n), key=lambda i: heights[i], reverse=True)
        for i, idx in enumerate(sorted_idx):
            names_[i] = names[idx]
        return names_