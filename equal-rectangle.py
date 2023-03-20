# author: birsnot - Nardos Wehabe

from collections import Counter


def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))


def solve():
    N = I()
    sides = Counter(SIL())
    sides = [[k, v] for k, v in sides.items()]
    area = sides[0][0]*sides[-1][0]
    l = 0
    r = len(sides) - 1
    ans = 0
    while l <= r:
        sidel = sides[l][0]
        sider = sides[r][0]
        check = sidel*sider
        if check != area:
            print("NO")
            return
        if sides[l][1] % 2 or sides[r][1] % 2:
            print("NO")
            return
        ans += 1
        sides[l][1] -= 2
        sides[r][1] -= 2
        if sides[l][1] == 0:
            l += 1
        if sides[r][1] == 0:
            r -= 1

    if ans == N:
        print("YES")
    else:
        print("NO")


T = I()
for ___ in range(T):
    solve()
