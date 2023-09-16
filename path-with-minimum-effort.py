class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R, C = len(heights), len(heights[0])
        edges = []
        for r in range(R):
            for c in range(C):
                if r < R - 1:
                    edges.append((abs(heights[r][c] - heights[r + 1][c]), (r, c), (r + 1, c)))
                if c < C - 1:
                    edges.append((abs(heights[r][c] - heights[r][c + 1]), (r, c), (r, c + 1)))
        edges.sort(key=lambda e: e[0])

        parent = {(r, c): (r, c) for r in range(R) for c in range(C)}

        def find(v):
            path = []
            while parent[v] != v:
                path.append(v)
                v = parent[v]
            for x in path:
                parent[x] = v
            return v

        st, end = (0, 0), (R - 1, C - 1)
        prev_c = 0
        for c, u, v in edges:
            if c != prev_c and find(st) == find(end):
                return prev_c
            parent[find(u)] = find(v)
            prev_c = c
        return prev_c