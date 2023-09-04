class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
    
        def get_order(condition):
            indegree = [0]*(k + 1)
            childs = defaultdict(list)
            for p, ch in condition:
                childs[p].append(ch)
                indegree[ch] += 1
            dq = deque()
            for i in range(1, k + 1):
                if indegree[i] == 0:
                    dq.append(i)
            pos = {}
            while dq:
                v = dq.popleft()
                pos[v] = len(pos)
                for ch in childs[v]:
                    indegree[ch] -= 1
                    if indegree[ch] == 0:
                        dq.append(ch)
            return pos
        
        row_pos = get_order(rowConditions)
        if len(row_pos) < k:
            return []
        col_pos = get_order(colConditions)
        if len(col_pos) < k:
            return []
        ans = [[0]*k for _ in range(k)]
        for i in range(1, k + 1):
            ans[row_pos[i]][col_pos[i]] = i
        return ans