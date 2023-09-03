class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        visited = {}
        ans = -1

        for i in range(len(edges)):
            if edges[i] != -1 and i not in visited:
                visited[i] = i
                nxt = edges[i]
                stack = [i]
                while edges[nxt] != -1 and nxt not in visited:
                    visited[nxt] = i
                    stack.append(nxt)
                    nxt = edges[nxt]
                if edges[nxt] != -1 and visited[nxt] == i:
                    ans = max(ans, len(stack) - stack.index(nxt))
        return ans