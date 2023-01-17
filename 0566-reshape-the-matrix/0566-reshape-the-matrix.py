class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        if r*c != rows*cols:
            return mat
        ans = [[0]*c for _ in range(r)]
        cur = 0
        for row in mat:
            for val in row:
                ans[cur//c][cur%c] = val
                cur += 1
        return ans