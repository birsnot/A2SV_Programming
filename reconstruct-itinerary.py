class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        childs = defaultdict(list)
        for p, ch in tickets:
            childs[p].append(ch)
        for p in childs:
            childs[p] = sorted(childs[p])
        N = len(tickets) + 1
        print(childs)
        ans = ["JFK"]
        def dfs(v):
            for i, ch in enumerate(childs[v]):
                if ch == "": continue
                ans.append(ch)
                childs[v][i] = ""
                if dfs(ch):
                    return True
                childs[v][i] = ch
                ans.pop()
            return len(ans) == N
        dfs("JFK")
        return ans