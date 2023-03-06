class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def helper(arr):
            N = len(arr) + 1
            ret = [0]*N
            ret[0] = ret[-1] = 1
            for i in range(1, N - 1):
                ret[i] = arr[i] + arr[i - 1]
            if N == rowIndex + 1:
                return ret
            return helper(ret)
        if rowIndex == 0: return [1]
        return helper([1])