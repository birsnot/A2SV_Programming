#User function Template for python3
from collections import defaultdict

class Solution:
    def findOrder(self,alien_dict, N, K):
        graph = defaultdict(set)
        prev = ""
        for s in alien_dict:
            i = 0
            while i < len(prev) and i < len(s):
                if prev[i] != s[i]:
                    graph[prev[i]].add(s[i])
                    break
                i += 1
            prev = s
        ans = []
        visited = defaultdict(int)
        def dfs(v):
            visited[v] = 1
            for ch in graph[v]:
                if visited[ch] == 0:
                    dfs(ch)
            ans.append(v)
        letters = "abcdefghijklmnopqrstuvwxyz"
        for ch in letters[:K]:
            if visited[ch] == 0:
                dfs(ch)
        ans.reverse()
        return ans
    # code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends