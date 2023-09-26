class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        trip_price = [0]*n

        end = -1        
        def dfs(v, p):
            if v == end:
                trip_price[v] += price[v] 
                return True
            for ch in adj[v]:
                if ch == p: continue
                if dfs(ch, v):
                    trip_price[v] += price[v]
                    return True
            return False
        
        for st, en in trips:
            end = en
            dfs(st, -1)

        dp = {}    

        def find(v, ok, p):
            if (v, ok) in dp:
                return dp[(v, ok)]
            take = leave = 0
            if ok:
                take = trip_price[v]//2
                for ch in adj[v]:
                    if ch == p: continue
                    take += find(ch, False, v)
            for ch in adj[v]:
                if ch == p: continue
                leave += find(ch, True, v)
            dp[(v, ok)] = max(take, leave)
            return dp[(v, ok)]

        ans = sum(trip_price) - find(0, True, -1)
        return ans