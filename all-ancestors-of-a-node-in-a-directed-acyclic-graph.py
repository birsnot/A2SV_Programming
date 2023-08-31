class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestors = defaultdict(set)
        childs = defaultdict(list)
        indegree = [0]*n
        dq = deque()
        for p, ch in edges:
            childs[p].append(ch)
            indegree[ch] += 1
        for v, d in enumerate(indegree):
            if d == 0:
                dq.append(v)
        while dq:
            p = dq.popleft()
            for ch in childs[p]:
                indegree[ch] -= 1
                ancestors[ch].update(ancestors[p])
                ancestors[ch].add(p)
                if indegree[ch] == 0:
                    dq.append(ch)
        ans = [[] for _ in range(n)]
        for v in ancestors:
            ans[v] = sorted(ancestors[v])
        return ans