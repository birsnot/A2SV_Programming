from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = [False]*V
        
        def dfs(v, p):
            visited[v] = True
            for ch in adj[v]:
                if ch == p: continue
                if not visited[ch]:
                    if not dfs(ch, v):
                        return False
                else:
                    return False
            return True
            
        for v in range(V):
            if not visited[v] and not dfs(v, -1):
                return True
        return False

#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends