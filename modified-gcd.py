# author: birsnot - Nardos Wehabe

from bisect import bisect_left
from collections import defaultdict
from sys import stdin
# def input(): return stdin.readline()[:-1]
input = stdin.readline
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))


def solve():
    A, B = II()
    Q = I()
    qr = []
    for _ in range(Q):
        qr.append(tuple(II()))
    fct1 = defaultdict(int)
    fct2 = defaultdict(int)
    n = 2
    a = A
    while n*n <= a:
        while a%n == 0:
            fct1[n] += 1
            a //= n
        n += 1
    if a > 1:
        fct1[a] += 1
    n = 2
    b = B
    while n*n <= b:
        while b%n == 0:
            fct2[n] += 1
            b //= n
        n += 1
    if b > 1:
        fct2[b] += 1
    cmn = {}
    for n in fct1:
        if n in fct2:
            cmn[n] = min(fct1[n], fct2[n])
    cmns = [1]
    for n in cmn:
        L = len(cmns)
        for i in range(cmn[n]):
            m = n**(i + 1)
            for j in range(L):
                cmns.append(cmns[j]*m)
    cmns.sort()
    for a, b in qr:
        idx = bisect_left(cmns, b)
        if idx >= len(cmns) or cmns[idx] > b:
            idx -= 1
        check = cmns[idx]
        if a <= check <= b:
            print(check)
        else:
            print(-1)

# T = I()
T = 1
for ___ in range(T):
    solve()
