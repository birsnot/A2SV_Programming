# author: birsnot - Nardos Wehabe

from collections import defaultdict
from sys import setrecursionlimit, stdin
# def input(): return stdin.readline()[:-1]
input = stdin.readline
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))
setrecursionlimit(100000)

def solve():
    N = I()
    childs = defaultdict(list)
    parent = [0]*(N + 1)
    for i in range(1, N + 1):
        p = I()
        parent[i] = p
        if p != -1:
            childs[p].append(i)

    def dfs(i):
        ret = 0
        for ch in childs[i]:
            ret = max(ret, dfs(ch))
        return ret + 1

    ans = 0
    for i in range(1, N + 1):
        if parent[i] == -1:
            ans = max(ans, dfs(i))
    print(ans)


# T = I()
T = 1
for ___ in range(T):
    solve()
