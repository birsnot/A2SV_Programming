from collections import defaultdict, deque

def parallelCourses(n, prerequisites):
    indegree = [0]*n
    childs = defaultdict(list)
    for p, ch in prerequisites:
        p, ch = p - 1, ch - 1
        indegree[ch] += 1
        childs[p].append(ch)
    dq = deque()
    for v, d in enumerate(indegree):
        if d == 0:
            dq.append(v)
    cnt = 0
    time = [1]*n
    while dq:
        v = dq.popleft()
        cnt += 1
        for ch in childs[v]:
            indegree[ch] -= 1
            time[ch] = max(time[ch], time[v] + 1)
            if indegree[ch] == 0:
                dq.append(ch)
    if cnt < n:
        return -1
    return max(time)