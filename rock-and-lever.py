# author: birsnot - Nardos Wehabe

from collections import defaultdict
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
        ans += 1
        n >>= 1
    return ans

def solve():
    N = I()
    nums = IL()
    check = defaultdict(int)
    ans = 0
    for n in nums:
        m = count(n)
        ans += check[m]
        check[m] += 1
    print(ans)
T = I()
for ___ in range(T):
    solve()
