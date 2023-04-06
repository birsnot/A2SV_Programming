# author: birsnot - Nardos Wehabe

from sys import stdin
# def input(): return stdin.readline()[:-1]
input = stdin.readline
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))


def solve():
    N = I()
    graph = [[] for _ in range(N + 1)]
    def add(u, v):
        graph[u].append(v)
        graph[v].append(u)
    def get_adj(u):
        print(*graph[u])
    M = I()
    for _ in range(M):
        opr = input()
        if opr[0] == "1":
            _, u, v = map(int, opr.split())
            add(u, v)
        else:
            u = int(opr.split()[1])
            get_adj(u)

T = 1
for ___ in range(T):
    solve()