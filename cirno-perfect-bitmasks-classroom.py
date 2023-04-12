# author: birsnot - Nardos Wehabe

def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))


def solve():
    N = n = I()
    first1 = 0
    while not n & 1:
        first1 += 1
        n >>= 1
    ans = 1 << first1
    if ans ^ N:
        print(ans)
    else:
        n = N
        first0 = 0
        while not n ^ 1:
            first0 += 1
            n >>= 1
        ans |= 1 << first0
        print(ans)


T = I()
for ___ in range(T):
    solve()