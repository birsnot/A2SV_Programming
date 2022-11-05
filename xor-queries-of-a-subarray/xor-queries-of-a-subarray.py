class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        N = len(arr)
        ps = [0]*(N+1)
        temp = 0
        for i, n in enumerate(arr,1):
            temp ^= n
            ps[i] = temp
        ans = [0]*len(queries)
        for i, q in enumerate(queries):
            ans[i] = ps[q[0]]^ps[q[1]+1]
        return ans
