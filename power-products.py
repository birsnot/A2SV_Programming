# author: birsnot - Nardos Wehabe

from collections import defaultdict
from sys import stdin
# def input(): return stdin.readline()[:-1]
input = stdin.readline
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))

def calc(n, k):
    ret1 = ret2 = 1
    d = 2
    while d*d <= n:
        if n%d == 0:
            count = 0
            while n%d == 0:
                count += 1
                n //= d
            ret1 *= d**(count%k)
            ret2 *= d**((-count)%k)
        d += 1
    if n > 1:
        ret1 *= n
        ret2 *= n**(k - 1)
    return ret1, ret2

        

def solve():
    N, K = II()
    nums = IL()
    d = defaultdict(int)
    ans = 0
    for n in nums:
        cur, check = calc(n, K)
        ans += d[check]
        d[cur] += 1
    print(ans)


# T = I()
T = 1
for ___ in range(T):
    solve()
