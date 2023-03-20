# author: birsnot - Nardos Wehabe

def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()), reverse=True)


def solve():
    N, M, K = II()
    emotes = SIL()
    times = M//(K + 1)
    ans = emotes[1]*times
    times = M - times
    ans += emotes[0]*times
    print(ans)


T = 1
for ___ in range(T):
    solve()
