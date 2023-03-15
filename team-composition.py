# author: birsnot - Nardos Wehabe

def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))


def solve():
    a, b = II()
    total = a + b
    min_ = min(a, b)

    def check(n):
        return n*4 <= total

    l = 0
    r = min_
    while l <= r:
        mid = (l + r)//2
        if check(mid):
            l = mid + 1
        else:
            r = mid - 1
    print(r)


T = I()
for ___ in range(T):
    solve()
