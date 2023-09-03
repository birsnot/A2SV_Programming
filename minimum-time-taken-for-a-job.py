from typing import List
from collections import defaultdict, deque

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        time = [1]*n
        indegree = [0]*n
        childs = defaultdict(list)
        for p, ch in edges:
            p, ch = p - 1, ch - 1
            indegree[ch] += 1
            childs[p].append(ch)
        dq = deque()
        for i, d in enumerate(indegree):
            if d == 0:
                dq.append(i)
        while dq:
            for _ in range(len(dq)):
                v = dq.popleft()
                for ch in childs[v]:
                    time[ch] = max(time[ch], time[v] + 1)
                    indegree[ch] -= 1
                    if indegree[ch] == 0:
                        dq.append(ch)
        return time


#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        IntArray().Print(res)
        

# } Driver Code Ends