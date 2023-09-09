class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        ans = N
        inc = []
        prev = ratings[0]
        for n in ratings:
            if n > prev:
                inc.append(inc[-1] + 1)
            else:
                inc.append(0)
            prev = n
        last = 0
        for i in range(N - 1, -1, -1):
            if ratings[i] > prev:
                last = last + 1
            else:
                last = 0
            prev = ratings[i]
            ans += max(last, inc[i])
        return ans