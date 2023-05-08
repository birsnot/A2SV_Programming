# author: birsnot - Nardos Wehabe

from sys import stdin
# def input(): return stdin.readline()[:-1]
input = stdin.readline
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))


def count(n):
    ans = 0
    while n > 0:
        ans += n&1
        n >>= 1
    return ans

def solve():
    n = I()
    print(count(n))
    
T = 1
for ___ in range(T):
    solve()
