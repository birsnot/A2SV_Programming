# author: birsnot - Nardos Wehabe

from sys import stdin
# def input(): return stdin.readline()[:-1]
input = stdin.readline
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))


def solve():
    N, K = II()
    if K > N:
        print("NO")
        return
    n = N
    ans = []
    count = 1
    while n > 0:
        if n&1:
            ans.append(count)
        n >>= 1
        count *= 2
    if len(ans) > K:
        print("NO")
        return
    print("YES")
    i = 0
    while len(ans) < K:
        while ans[i] == 1:
            i += 1
        ans[i] //= 2
        ans.append(ans[i])
    print(*sorted(ans))

T = 1
for ___ in range(T):
    solve()
