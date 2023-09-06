class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        N = len(accounts)
        parent = list(range(N))
        size = [1]*N
        visited = {}

        def find(v):
            stack = []
            while parent[v] != v:
                stack.append(v)
                v = parent[v]
            for x in stack:
                parent[x] = v
            return v
        
        def union_(u, v):
            pu = find(u)
            pv = find(v)
            if pu == pv: return
            if size[pv] > size[pu]:
                parent[pu] = pv
                size[pv] += size[pu]
                size[pu] = 0
            else:
                parent[pv] = pu
                size[pu] += size[pv]
                size[pv] = 0

        for i, ac in enumerate(accounts):
            for email in ac[1:]:
                if email in visited:
                    union_(visited[email], i)
                else:
                    visited[email] = i
        same = defaultdict(list)
        for email in visited:
            same[find(visited[email])].append(email)
        ans = []
        for i in same:
            temp = [accounts[i][0]]
            temp.extend(sorted(same[i]))
            ans.append(temp)
        return ans