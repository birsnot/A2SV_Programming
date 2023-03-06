# author: birsnot - Nardos Wehabe

def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))


def solve():
    N, M = II()
    outlets = SIL()
    sofar = 2
    ans = 0
    if N <= sofar:
        print(ans)
        return
    for n in outlets[::-1]:
        sofar += (n-1)
        ans += 1
        if N <= sofar:
            print(ans)
            return
    print(-1)

T = I()
for ___ in range(T):
    solve()
