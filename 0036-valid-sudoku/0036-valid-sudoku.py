class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            nums = set()
            for val in row:
                if val != ".":
                    if val in nums:
                        return False
                    else:
                        nums.add(val)
        for col in zip(*board):
            nums = set()
            for val in col:
                if val != ".":
                    if val in nums:
                        return False
                    else:
                        nums.add(val)
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                nums = set()
                for i in range(9):
                    val = board[r + i//3][c + i%3]
                    if val != ".":
                        if val in nums:
                            return False
                        else:
                            nums.add(val)
        return True