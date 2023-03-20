# author: birsnot - Nardos Wehabe

from collections import Counter


def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))


def eq(n1, n2):
    return abs(n1 - n2) < 1e-8 or abs(n1 - n2) > 10**12


def solve():
    recipe = Counter(input())
    nb, ns, nc = II()
    pb, ps, pc = II()
    r = I()
    if not recipe["B"]:
        nb = 10**16
        recipe["B"] = 0.0001
    if not recipe["S"]:
        ns = 10**16
        recipe["S"] = 0.0001
    if not recipe["C"]:
        nc = 10**16
        recipe["C"] = 0.0001
    rb = nb/recipe["B"]
    rs = ns/recipe["S"]
    rc = nc/recipe["C"]
    while (not eq(rb, rs) or not eq(rs, rc)) and r:
        if rb < rs:
            if rb < rc:
                if pb > r:
                    print(min(nb//recipe["B"], ns //
                          recipe["S"], nc//recipe["C"]))
                    return
                else:
                    r -= pb
                    nb += 1
            else:
                if pc > r:
                    print(min(nb//recipe["B"], ns //
                          recipe["S"], nc//recipe["C"]))
                    return
                else:
                    r -= pc
                    nc += 1
        else:
            if rs < rc:
                if ps > r:
                    print(min(nb//recipe["B"], ns //
                          recipe["S"], nc//recipe["C"]))
                    return
                else:
                    r -= ps
                    ns += 1
            else:
                if pc > r:
                    print(min(nb//recipe["B"], ns //
                          recipe["S"], nc//recipe["C"]))
                    return
                else:
                    r -= pc
                    nc += 1
        rb = nb/recipe["B"]
        rs = ns/recipe["S"]
        rc = nc/recipe["C"]
    needed = 0
    if recipe["B"] >= 1:
        needed += recipe["B"]*pb
    if recipe["C"] >= 1:
        needed += recipe["C"]*pc
    if recipe["S"] >= 1:
        needed += recipe["S"]*ps
    add_ = r//needed
    ans = add_ + (min(nb//recipe["B"], ns//recipe["S"], nc//recipe["C"]))
    print(ans)


T = 1
for ___ in range(T):
    solve()
