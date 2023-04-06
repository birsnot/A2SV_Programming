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
    sinks = []
    sources = []
    adjm = []
    for i in range(1, N + 1):
        row = IL()
        adjm.append(row)
        if sum(row) == 0:
            sinks.append(i)
    for i, col in enumerate(zip(*adjm), 1):
        if sum(col) == 0:
            sources.append(i)
    print(len(sources), *sources)
    print(len(sinks), *sinks)

T = 1
for ___ in range(T):
    solve()