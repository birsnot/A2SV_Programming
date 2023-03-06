# author: birsnot - Nardos Wehabe

from itertools import accumulate


def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))


def solve():
    N = I()
    ps = IL()
    ps = list(accumulate(ps, initial=0))
    if N <= 12:
        print(ps[-1])
        return
    if N <= 18:
        print(min(ps[12], ps[-1] - ps[12]))
        return
    ans = min(ps[12], ps[18])
    n = 12
    while N > n + 12:
        ans = min(ans, ps[n+12] - ps[n])
        if N > n + 18:
            ans = min(ans, ps[n+18] - ps[n])
        n += 6
    if N > n + 6:
        n += 6
    ans = min(ans, ps[-1] - ps[n])
    print(ans)


T = I()
for ___ in range(T):
    solve()
