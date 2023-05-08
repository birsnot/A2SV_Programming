# author: birsnot - Nardos Wehabe

from sys import stdin
# def input(): return stdin.readline()[:-1]
input = stdin.readline
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))

def seive(n):
    n += 1
    ans = [1]*n
    ans[0] = ans[1] = 2
    for i in range(4, n, 2):
        ans[i] = 2
    i = 3
    while i*i < n:
        if ans[i]:
            for j in range(i*i, n, i):
                ans[j] = 2
        i += 2
    return ans

def solve():
    N = I()
    if N < 3:
        print(1)
    else:
        print(2)
    print(*seive(N+1)[2:])

# T = I()
T = 1
for ___ in range(T):
    solve()
