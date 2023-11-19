class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for (u, v), val in zip(equations, values):
            adj[u].append((v, val))
            adj[v].append((u, 1/val))
        
        deno = ""
        visited = set()
        def dfs(v, val):
            visited.add(v)
            ret = -1
            for ch, cur in adj[v]:
                if ch in visited: continue
                if ch == deno:
                    return val*cur
                ret = dfs(ch, val*cur)
                if ret > 0:
                    return ret
            return -1

        ans = []        
        for u, v in queries:
            if u not in adj or v not in adj:
                ans.append(-1)
            elif u == v:
                ans.append(1)
            else:
                deno = v
                visited = set()
                ans.append(dfs(u, 1))
        return ans