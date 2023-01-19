class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            nums = [0]*10
            for val in row:
                if val != ".":
                    val = int(val)
                    if nums[val]:
                        return False
                    else:
                        nums[val] = 1
        for col in zip(*board):
            nums = [0]*10
            for val in col:
                if val != ".":
                    val = int(val)
                    if nums[val]:
                        return False
                    else:
                        nums[val] = 1
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                nums = [0]*10
                for i in range(9):
                    val = board[r + i//3][c + i%3]
                    if val != ".":
                        val = int(val)
                        if nums[val]:
                            return False
                        else:
                            nums[val] = 1
        return True