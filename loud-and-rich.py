class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        N = len(quiet)
        indegree = [0]*N
        childs = defaultdict(list)
        for p, ch in richer:
            childs[p].append(ch)
            indegree[ch] += 1
        dq = deque()
        for i, d in enumerate(indegree):
            if d == 0:
                dq.append(i)
        ans = list(range(N))
        while dq:
            v = dq.popleft()
            for ch in childs[v]:
                ans[ch] = min(ans[ch], ans[v], key=lambda x: quiet[x])
                indegree[ch] -= 1
                if indegree[ch] == 0:
                    dq.append(ch)
        return ans