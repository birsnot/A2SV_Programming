class Solution:
    def candy(self, ratings: List[int]) -> int:
        change = [0]*len(ratings)
        for i, n in enumerate(ratings[1:]):
            if ratings[i] < n:
                change[i+1] = change[i] + 1
            elif ratings[i] > n:
                change[i+1] = change[i] - 1
            else:
                change[i+1] = change[i]
        pivots = []
        prev = "a"
        for i, n in enumerate(change):
            if n == prev:
                pivots.append(i)
            prev = n
        pivots.append(len(ratings))
        ans = [0]*len(ratings)
        prev_p = 0
        for p in pivots:
            mounts = []
            i = prev_p + 1
            up = False
            while i < p:
                if not up and change[i] > change[i-1]:
                    up = True
                elif up and change[i] < change[i-1]:
                    up = False
                    mounts.append(i)
                i += 1
            mounts.append(p)
            prev_m = prev_p
            for m in mounts:
                sub = change[prev_m:m]
                min_ = min(sub)
                ans[prev_m] = max(ans[prev_m], change[prev_m] - min_)
                i = prev_m + 1
                while i < m:
                    ans[i] = change[i] - min_
                    i += 1
                # ans[m-1] = max(ans[m-1], change[m-1] - min_)
                prev_m = m - 1
            if prev_p < len(ratings)-1 and change[prev_p] < change[prev_p + 1]:
                ans[prev_p] = 0
            if p > 1 and change[p-1] < change[p-2]:
                change[p-1] = 0
                
            prev_p = p
        
        
        return sum(ans) + len(ratings)