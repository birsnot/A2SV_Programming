# author: birsnot - Nardos Wehabe


from collections import defaultdict, deque
from sys import setrecursionlimit, stdin
# from threading import Thread, stack_size
def input(): return stdin.readline()[:-1]
# input = stdin.readline
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))

def solve():
    N = I()
    names = []
    for _ in range(N):
        names.append(input())
    adj = defaultdict(set)
    for i in range(N - 1):
        j = 0
        N1, N2 = len(names[i]), len(names[i + 1])
        while j < N1 and j < N2 and names[i][j] == names[i + 1][j]:
            j += 1
        if j >= N2:
            print("Impossible")
            return
        if j < N1:
            adj[names[i][j]].add(names[i + 1][j])
    visited = {}
    cur = []
    def dfs(v):
        visited[v] = 1
        for ch in adj[v]:
            if ch not in visited:
                if not dfs(ch):
                    return False
            elif visited[ch] == 1:
                return False
        visited[v] = 2
        cur.append(v)
        return True
    letters = "abcdefghijklmnopqrstuvwxyz"
    ans = ""
    for v in letters:
        if v not in visited:
            if not dfs(v):
                print("Impossible")
                return
    ans = "".join(reversed(cur))
    print(ans)

    

def main():
    # T = I()
    T = 1
    for ___ in range(T):
        solve()

main()

# setrecursionlimit(100050)
# stack_size(1<<27)
# _mt = Thread(target=main)
# _mt.start()
# _mt.join()