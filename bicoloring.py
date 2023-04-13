# author: birsnot - Nardos Wehabe

from collections import defaultdict
from sys import setrecursionlimit, stdin
# def input(): return stdin.readline()[:-1]
input = stdin.readline
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))
# setrecursionlimit(1<<30)

def solve(N):
    adj = defaultdict(list)
    E = I()
    for _ in range(E):
        u, v = II()
        adj[u].append(v)
        adj[v].append(u)
    visited = [0]*(N+1)
    def dfs(u, p):
        color = visited[p]^3
        visited[u] = color
        for v in adj[u]:
            if visited[v]:
                if visited[v] != color or v == p: continue
                else: return False
            else:
                if not dfs(v, u):
                    return False
        return True
    visited[0] = 1
    if dfs(1, 0):
        print("BICOLOURABLE.")
    else:
        print("NOT BICOLOURABLE.")

T = I()
while T:
    solve(T)
    T = I()