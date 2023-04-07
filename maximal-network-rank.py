class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # author - Nardos Wehabe
        if len(roads) == (n*(n - 1))//2: return 2*n - 3
        if len(roads) < 3: return len(roads)
        dgr = [0]*n
        adjM = [[0]*n for _ in range(n)]
        for u, v in roads:
            dgr[u] += 1
            dgr[v] += 1
            adjM[u][v] = adjM[v][u] = 1
        mxs = sorted(range(n), key=lambda i: dgr[i], reverse=True)
        maxU = dgr[mxs[0]]
        maxV = dgr[mxs[1]]
        ans = 0
        for u in range(n):
            if dgr[mxs[u]] < maxU:
                break
            for v in range(u + 1, n):
                if dgr[mxs[v]] < maxV:
                    break
                if adjM[mxs[u]][mxs[v]] == 1:
                    ans = dgr[mxs[u]] + dgr[mxs[v]] - 1
                else:
                    return dgr[mxs[u]] + dgr[mxs[v]]
        return ans