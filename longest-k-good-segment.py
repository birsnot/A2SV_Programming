# author: birsnot - Nardos Wehabe

from collections import defaultdict


def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))


def solve():
    N, K = II()
    nums = IL()
    ans = -1
    ans_i = (0, 0)
    l = 0
    s = defaultdict(int)
    for i, n in enumerate(nums):
        s[n] += 1
        while len(s) > K:
            s[nums[l]] -= 1
            if s[nums[l]] == 0:
                del s[nums[l]]
            l += 1

        if i - l > ans:
            ans = i - l
            ans_i = (l + 1, i + 1)
    print(*ans_i)


T = 1
for ___ in range(T):
    solve()
