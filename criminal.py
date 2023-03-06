# author: birsnot - Nardos Wehabe

def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))


def solve():
    N = I()
    evils = IL()
    ptr = 0
    while ptr < N and evils[ptr] == 0:
        ptr += 1
    ans = 0
    for n in evils[ptr:-1]:
        if n == 0:
            ans += 1
        else:
            ans += n
    print(ans)
    
T = I()
for ___ in range(T):
    solve()
