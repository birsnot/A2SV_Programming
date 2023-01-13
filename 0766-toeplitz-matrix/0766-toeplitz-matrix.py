class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        diags = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                key = r - c
                if key in diags:
                    if diags[key] != val:
                        return False
                else:
                    diags[key] = val
        return True