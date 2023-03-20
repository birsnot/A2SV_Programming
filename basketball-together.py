# author: birsnot - Nardos Wehabe

from collections import deque
from math import ceil


def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))


def solve():
    N, D = II()
    nums = deque(SIL())
    ans = 0
    while nums:
        n = nums.pop()
        needed = D//n
        if len(nums) >= needed:
            ans += 1
            for _ in range(needed):
                nums.popleft()
        else:
            break
    print(ans)


T = 1
for ___ in range(T):
    solve()
