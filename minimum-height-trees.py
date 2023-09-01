class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        degree = [0]*n
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1

        dq = deque()
        for i, d in enumerate(degree):
            if d <= 1:
                dq.append(i)
                n -= 1
        
        while n:
            for _ in range(len(dq)):
                v = dq.popleft()
                for ch in adj[v]:
                    degree[ch] -= 1
                    if degree[ch] == 1:
                        dq.append(ch)
                        n -= 1
        return dq