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
    nums = IL()
    def merge(l, r):
        if l == r:
            return [l]
        mid = (r + l)//2
        left = merge(l, mid)
        right = merge(mid + 1, r)
        if nums[left[-1]] + K < nums[right[-1]]:
            left, right = right, left
        while right and nums[right[-1]] + K < nums[left[-1]]:
            right.pop()
        p1, p2, ret = 0, 0, []
        while p1 < len(left) and p2 < len(right):
            if nums[left[p1]] >= nums[right[p2]]:
                ret.append(left[p1])
                p1 += 1
            else:
                ret.append(right[p2])
                p2 += 1
        ret.extend(left[p1:])
        ret.extend(right[p2:])
        return ret
    ans = merge(0, (1<<N) - 1)
    ans = sorted(map(lambda x: x + 1, ans))
    print(*ans)

T = 1
for ___ in range(T):
    solve()