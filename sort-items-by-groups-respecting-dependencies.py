class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
        g_indegree = [0]*m
        i_indegree = [0]*n
        g_childs = defaultdict(list)
        i_childs = defaultdict(list)
        for i, before in enumerate(beforeItems):
            g = group[i]
            for p in before:
                if group[p] != g:
                    g_indegree[g] += 1
                    g_childs[group[p]].append(g)
                else:
                    i_indegree[i] += 1
                    i_childs[p].append(i)
        group_order = []
        dq = deque()
        for g, d in enumerate(g_indegree):
            if d == 0:
                dq.append(g)
        while dq:
            g = dq.popleft()
            group_order.append(g)
            for ch in g_childs[g]:
                g_indegree[ch] -= 1
                if g_indegree[ch] == 0:
                    dq.append(ch)
        if len(group_order) < m:
            return []
        order = defaultdict(list)
        dq = deque()
        for i, d in enumerate(i_indegree):
            if d == 0:
                dq.append(i)
        while dq:
            i = dq.popleft()
            order[group[i]].append(i)
            for ch in i_childs[i]:
                i_indegree[ch] -= 1
                if i_indegree[ch] == 0:
                    dq.append(ch)
        ans = []
        for g in group_order:
            ans.extend(order[g])
        if len(ans) < n:
            return []
        return ans