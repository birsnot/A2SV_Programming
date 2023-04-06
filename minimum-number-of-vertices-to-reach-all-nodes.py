class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        sources = [1]*n
        for _, d in edges:
            sources[d] = 0
        ans = []
        for i, src in enumerate(sources):
            if src:
                ans.append(i)
        return ans