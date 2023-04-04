# author: birsnot - Nardos Wehabe

from sys import stdin
# def input(): return stdin.readline()[:-1]
input = stdin.readline
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))


def check(nums):
    count = 1
    for n in nums:
        if n == count:
            count += 1
        else:
            return False
    return True


def solve():
    N = I()
    nums = IL()
    ans = 0

    def helper(l, r):
        nonlocal ans
        if l == r:
            return [nums[l]]
        mid = (l + r) // 2
        left = helper(l, mid)
        right = helper(mid + 1, r)
        if left[0] > right[0]:
            ans += 1
            right.extend(left)
            return right
        left.extend(right)
        return left
    nums = helper(0, N - 1)
    if check(nums):
        print(ans)
    else:
        print(-1)

T = I()
for ___ in range(T):
    solve()