class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        for r, row in enumerate(grid):
            grid[r] = list(row)

        R, C = len(grid), len(grid[0])
        index = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}

        visited = set()
        dq = deque()
        total_keys = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '.' or grid[r][c] == '#' or grid[r][c].isupper():
                    continue
                if grid[r][c].islower():
                    total_keys |= 1<<index[grid[r][c]]
                else:
                    dq.append((r, c, 0))
                    visited.add((r, c, 0))
                    grid[r][c] = '.'
        
        drc = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        moves = 0
        while dq:
            moves += 1
            for _ in range(len(dq)):
                r, c, mask = dq.popleft()
                for dr, dc in drc:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < R and 0 <= nc < C and (grid[nr][nc] != '#') and ((nr, nc, mask) not in visited):
                        visited.add((nr, nc, mask))
                        if grid[nr][nc] == '.' :
                            dq.append((nr, nc, mask))
                        elif grid[nr][nc].islower():
                            new_mask = mask | (1<<index[grid[nr][nc]])
                            if new_mask == total_keys:
                                return moves
                            dq.append((nr, nc, new_mask))
                        elif mask&(1<<index[grid[nr][nc].lower()]):
                            dq.append((nr, nc, mask))
        return -1