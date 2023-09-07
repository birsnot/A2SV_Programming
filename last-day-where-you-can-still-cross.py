class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        parent = {(r, c): (r, c) for r in range(row) for c in range(col)}
        size = {(r, c): 1 for r in range(row) for c in range(col)}
        left = (0, 0)
        right = (0, col - 1)
        for r in range(1, row):
            parent[(r, 0)] = left
            parent[(r, col - 1)] = right
        
        size[left] = size[right] = row
        
        def find(v):
            path = []
            while parent[v] != v:
                path.append(v)
                v = parent[v]
            for x in path:
                parent[x] = v
            return v
        
        def union(u, v):
            pu = find(u)
            pv = find(v)
            if pu == pv: return
            if size[pu] > size[pv]:
                parent[pv] = pu
                size[pu] += size[pv]
            else:
                parent[pu] = pv
                size[pv] += size[pu]

        drc = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        grid = [[0]*col for _ in range(row)]

        for i, (r, c) in enumerate(cells):
            r, c = r - 1, c - 1
            grid[r][c] = 1
            for dr, dc in drc:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                    union((nr, nc), (r, c))
            if find(left) == find(right):
                return i
        return -1