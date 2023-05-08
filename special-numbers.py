# author: birsnot - Nardos Wehabe

from sys import stdin
# def input(): return stdin.readline()[:-1]
input = stdin.readline
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))


def solve():
    N, k = II()
    ans = 0
    count = 0
    while k > 0:
        ans += (N**count)*(k&1)
        count += 1
        k >>= 1
    print(ans%(1000000007))

T = I()
for ___ in range(T):
    solve()
