class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = []
        for i in range(n,1,-1):
            k = arr.index(i)
            ans.extend([k+1,i])
            arr = arr[:k:-1]+arr[:k]
        return ans
