class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        reqs = []
        within = 0
        for fr, to in requests:
            if fr == to: within += 1
            else: reqs.append([fr, to])
        N = len(reqs)
        ans = 0
        def helper(i, fr, d, ans_):
            nonlocal ans
            if reqs[i][1] == fr:
                ans_ += d
                ans = max(ans, ans_)
                return d
            to = reqs[i][1]
            for j in range(N):
                if reqs[j][0] == to:
                    reqs[j][0] -= 21
                    d_ = helper(j, fr, d+1, ans_)
                    temp = []
                    d__ = k = 0
                    while d_:
                        d__ += d_
                        d_ = 0
                        while k < N:
                            if reqs[k][0] > 0:
                                reqs[k][0] -= 21
                                temp.append(k)
                                d_ = helper(k, reqs[k][0] + 21, 1, ans_ + d__)
                                if d_: break
                            k += 1
                    for k in temp: reqs[k][0] += 21
                    reqs[j][0] += 21
            return 0
        for i, (fr, _) in enumerate(reqs):
            reqs[i][0] -= 21
            helper(i, fr, 1, 0)
            reqs[i][0] += 21
        return ans + within