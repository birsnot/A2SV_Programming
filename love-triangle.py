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
    for i, n in enumerate(nums, 1):
        if nums[nums[n - 1] - 1] == i:
            print("YES")
            return
    print("NO")


# T = I()
T = 1
for ___ in range(T):
    solve()
