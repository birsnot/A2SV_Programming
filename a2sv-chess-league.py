# author: birsnot - Nardos Wehabe

from itertools import product


def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))


def min(rat):
    min_ = (float("inf"), 1)
    for r in rat:
        if r[0] < min_[0]:
            min_ = r
    return min_


def solve():
    N, dif = II()
    ratings = IL()
    ratings = [[(ratings[i], i)] for i in range(len(ratings))]
    remain = N
    while remain > 0:
        M = len(ratings)
        temp2 = []
        for i in range(0, M, 2):
            temp = []
            min1 = min(ratings[i])
            min2 = min(ratings[i+1])
            for r in ratings[i+1]:
                if r[0] >= min1[0] - dif:
                    temp.append(r)
            for r in ratings[i]:
                if r[0] >= min2[0] - dif:
                    temp.append(r)
            if len(temp) > 0:
                temp2.append(temp)
        ratings = temp2
        remain -= 1
    ans = []
    for a in ratings[0]:
        ans.append(a[1] + 1)
    ans.sort()
    print(*ans)


T = 1
for ___ in range(T):
    solve()
    print()
