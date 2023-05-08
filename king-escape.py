# author: birsnot - Nardos Wehabe

from sys import setrecursionlimit, stdin
# def input(): return stdin.readline()[:-1]
input = stdin.readline
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))
setrecursionlimit(100000)

def cmp(n1, n2):
    if n1 < n2:
        return -1
    if n1 > n2:
        return 1
    return 0

def solve():
    N = I()
    ax, ay = II()
    bx, by = II()
    cx, cy = II()
    if cmp(bx, ax) == cmp(cx, ax) and cmp(by, ay) == cmp(cy, ay):
        print("YES")
    else:
        print("NO")


# T = I()
T = 1
for ___ in range(T):
    solve()
