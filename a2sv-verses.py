# author: birsnot - Nardos Wehabe

from itertools import accumulate


def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))

def count(ps, k):
    l = 0
    len_ = len(ps)
    i = 1
    ans = 0
    while i < len_:
        while i < len_ and ps[i] - ps[l] < k:
            ans += i - l
            i += 1
        while i < len_ and ps[i] - ps[l] >= k:
            l += 1
    return ans




def solve():
    N, a, b = II()
    nums = IL()
    ps = [0] + list(accumulate(nums))
    print(count(ps, b + 1) - count(ps, a))

T = 1
for ___ in range(T):
    solve()
