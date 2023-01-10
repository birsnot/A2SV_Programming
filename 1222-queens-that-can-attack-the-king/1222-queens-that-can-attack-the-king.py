class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        board = [[0]*8 for _ in range(8)]
        for r,c in queens:
            board[r][c] = 1
            
        krow, kcol = king
        ans = []
        
        #up
        r = krow - 1
        while r > -1:
            if board[r][kcol] == 1:
                ans.append([r, kcol])
                break
            r -= 1
        
        #down
        r = krow + 1
        while r < 8:
            if board[r][kcol] == 1:
                ans.append([r, kcol])
                break
            r += 1
            
        #left
        c = kcol - 1
        while c > -1:
            if board[krow][c] == 1:
                ans.append([krow, c])
                break
            c -= 1
        
        #right
        c = kcol + 1
        while c < 8:
            if board[krow][c] == 1:
                ans.append([krow, c])
                break
            c += 1
        
        #up_left
        c = kcol - 1
        r = krow - 1
        while c > -1 and r > -1:
            if board[r][c] == 1:
                ans.append([r, c])
                break
            r -= 1
            c -= 1
        
        #up_right
        c = kcol + 1
        r = krow - 1
        while c < 8 and r > -1:
            if board[r][c] == 1:
                ans.append([r, c])
                break
            r -= 1
            c += 1
        
        #down_right
        c = kcol + 1
        r = krow + 1
        while c < 8 and r < 8:
            if board[r][c] == 1:
                ans.append([r, c])
                break
            r += 1
            c += 1
        
        #down_left
        c = kcol - 1
        r = krow + 1
        while c > -1 and r < 8:
            if board[r][c] == 1:
                ans.append([r, c])
                break
            r += 1
            c -= 1
        
        return ans