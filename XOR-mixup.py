# author: birsnot - Nardos Wehabe

from sys import stdin
# def input(): return stdin.readline()[:-1]
input = stdin.readline
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))


def solve():
    N = I()
    nums = IL()
    a = 0
    for n in nums:
        a ^= n
    ans = 0
    for n in nums:
        if n == n^a:
            ans = n
            break
    print(ans)

T = I()
for ___ in range(T):
    solve()
