# author: birsnot - Nardos Wehabe

from collections import defaultdict
from sys import setrecursionlimit, stdin
# def input(): return stdin.readline()[:-1]
input = stdin.readline
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))
setrecursionlimit(100000)

def cnt(arr):
    res = defaultdict(int)
    temp = 0
    for n in arr:
        if n == 1:
            temp += 1
        else:
            res[temp] += 1
            temp = 0
    res[temp] += 1
    return res


def solve():
    N, M, K = II()
    a = IL()
    b = IL()
    cnta = cnt(a)
    cntb = cnt(b)
    cntbs = sorted(cntb, reverse=True)
    dp = [0]*(max(cnta) + 1)
    for i in range(1, max(cnta) + 1):
        cur = 0
        if K%i == 0:
            m = K//i
            for c in cntbs:
                if c >= m:
                    cur += (c + 1 - m)*cntb[c]
                else:
                    break
        cur += dp[i - 1]*2 - dp[i - 2]
        dp[i] = cur
    ans = 0
    for c in cnta:
        ans += dp[c]*cnta[c]
    print(ans)

# T = I()
T = 1
for ___ in range(T):
    solve()
