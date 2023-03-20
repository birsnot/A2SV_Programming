# author: birsnot - Nardos Wehabe

from itertools import accumulate


def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))


def solve():
    N, M = II()
    line = [0]*(N+1)
    for _ in range(M):
        l, r = II()
        line[l] += 1
        line[r + 1] -= 1
    prev = 0
    for i in range(len(line)):
        line[i] += prev
        prev = line[i]
    line.pop()
    c = line.count(0)
    if c == 0:
        print("NO")
    else:
        print("YES")


T = 1
for ___ in range(T):
    solve()
