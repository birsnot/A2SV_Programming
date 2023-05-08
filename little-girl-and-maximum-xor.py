# author: birsnot - Nardos Wehabe

from sys import stdin
# def input(): return stdin.readline()[:-1]
input = stdin.readline
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))

def log(n):
    ans = 1
    while n > 1:
        ans *= 2
        n >>= 1
    return ans

def solve():
    L, R = II()
    if L == R:
        print(0)
        return
    def isok(n): return n >= L and n <= R
    m = log(R)
    n = m
    while (not isok(n) or not isok(n-1)) and (m > 1):
        m = log(R - n)
        n += m
    print(n^(n-1))

T = 1
for ___ in range(T):
    solve()
