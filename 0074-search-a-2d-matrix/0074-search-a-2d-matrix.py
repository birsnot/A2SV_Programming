class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.target = target
        self.matrix = matrix
        return self.binary_search(0, self.n*self.m - 1)
    
    def binary_search(self, st, end):
        if st >= end:
            return self.matrix[st//self.n][st%self.n] == self.target
        mid = (st + end)//2
        val = self.matrix[mid//self.n][mid%self.n]
        if val == self.target:
            return True
        elif val < self.target:
            return self.binary_search(mid + 1, end)
        else:
            return self.binary_search(st, mid - 1)