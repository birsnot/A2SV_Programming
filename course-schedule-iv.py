class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        indegree = [0]*numCourses
        childs = defaultdict(list)
        for p, ch in prerequisites:
            childs[p].append(ch)
            indegree[ch] += 1
        dq = deque()
        for i, d in enumerate(indegree):
            if d == 0:
                dq.append(i)
        parents = defaultdict(set)
        while dq:
            v = dq.popleft()
            for ch in childs[v]:
                parents[ch].update(parents[v])
                parents[ch].add(v)
                indegree[ch] -= 1
                if indegree[ch] == 0:
                    dq.append(ch)
        ans = []
        for p, ch in queries:
            ans.append(p in parents[ch])
        return ans