# author: birsnot - Nardos Wehabe

from math import gcd, sqrt
from sys import stdin
# def input(): return stdin.readline()[:-1]
input = stdin.readline
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))

def solve():
    N = I()
    n = int(sqrt(N))
    if n*n <= N:
        n += 1
    while n > 0:
        if N%n == 0 and gcd(n, N//n) == 1:
            print(min(n, N//n), max(n, N//n))
            return
        n -= 1
    print(1, N)

# T = I()
T = 1
for ___ in range(T):
    solve()
