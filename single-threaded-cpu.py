class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        pq = []
        ans = []
        N = len(tasks)
        idxes = sorted(range(N), key=lambda i: tasks[i])
        cur = 1
        i = 0
        while pq or i < N:
            if not pq:
                cur = max(tasks[idxes[i]][0], cur)
            while i < N and tasks[idxes[i]][0] <= cur:
                heappush(pq, (tasks[idxes[i]][1], idxes[i]))
                i += 1
            proc, idx = heappop(pq)
            cur += proc
            ans.append(idx)
        return ans