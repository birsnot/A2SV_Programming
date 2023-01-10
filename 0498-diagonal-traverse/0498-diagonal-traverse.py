class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        m = len(mat)
        n = len(mat[0])
        ans_len = m*n
        ans = []
        r = c = 0
        while len(ans) < ans_len:
            
            #move up and right
            while r > -1 and c < n:
                ans.append(mat[r][c])
                r -= 1
                c += 1
            if c == n:
                r += 2
                c -= 1
            else:
                r += 1
            
            if len(ans) == ans_len:
                break
                
            #move down and left
            while r < m and c > -1:
                ans.append(mat[r][c])
                r += 1
                c -= 1
            if r == m:
                c += 2
                r -= 1
            else:
                c += 1
        
        return ans