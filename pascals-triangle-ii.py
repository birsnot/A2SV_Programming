class Solution:
    def getRow(self, n: int) -> List[int]:
        def helper(arr):
            prev = 1
            N = len(arr)
            for i in range(1, N):
                temp = prev
                prev = arr[i]
                arr[i] += temp
            arr.append(1)
            if N == n:
                return arr
            return helper(arr)
        if n == 0: return [1]
        return helper([1])