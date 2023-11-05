class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr) - 1: return max(arr)
        max_ = arr[0]
        cnt = 0
        for n in arr[1:]:
            if n > max_:
                cnt = 1
                max_ = n
            else:
                cnt += 1
            if cnt == k:
                return max_
        return max_