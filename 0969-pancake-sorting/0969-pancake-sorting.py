class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        # n = len(arr)
        # ans = []
        # for i in range(n,1,-1):
        #     k = arr.index(i)
        #     ans.extend([k+1,i])
        #     arr = arr[:k:-1]+arr[:k]
        # return ans
        n = len(arr)
        ans = []
        for i in range(n, 0, -1):
            if arr[i - 1] != i:
                idx = arr.index(i) + 1
                arr = arr[:idx][::-1] + arr[idx:]
                arr = arr[:i][::-1] + arr[i:]
                ans.append(idx)
                ans.append(i)
        return ans