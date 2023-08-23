class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        dq = deque()
        drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def dfs(r, c):
            for dr, dc in drc:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    dq.append((nr, nc))
                    dfs(nr, nc)
        found = False
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    grid[r][c] = 2
                    dq.append((r, c))
                    dfs(r, c)
                    found = True
                    break
            if found:
                break
        flips = -1
        while dq:
            flips += 1
            for _ in range(len(dq)):
                r, c = dq.popleft()
                for dr, dc in drc:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < N and 0 <= nc < N:
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = 2
                            dq.append((nr, nc))
                        elif grid[nr][nc] == 1:
                            return flips