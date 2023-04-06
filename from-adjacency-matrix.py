# author: birsnot - Nardos Wehabe

from collections import defaultdict
from sys import stdin
# def input(): return stdin.readline()[:-1]
input = stdin.readline
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))


def solve():
    N = I()
    adj = [[] for _ in range(N)]
    for u in range(N):
        for v, w in enumerate(II(), 1):
            if w:
                adj[u].append(v)
    for u in adj:
        print(len(u), *u)

T = 1
for ___ in range(T):
    solve()