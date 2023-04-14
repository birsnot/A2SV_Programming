class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        c0 = image[sr][sc]
        if c0 == color:
            return image
        M = len(image)
        N = len(image[0])
        def dfs(r, c):
            image[r][c] = color
            drc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dr, dc in drc:
                nr, nc = r + dr, c + dc
                if -1 < nr < M and -1 < nc < N and image[nr][nc] == c0:
                    dfs(nr, nc)
        dfs(sr, sc)
        return image