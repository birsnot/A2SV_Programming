# author: birsnot - Nardos Wehabe


def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))


def solve():
    N, M = II()
    infected = SIL()
    uninfected = [infected[0] - 1 + N - infected[-1]]
    for i in range(len(infected) - 1):
        uninfected.append(infected[i+1] - infected[i] - 1)
    uninfected.sort(reverse=True)
    ans = 0
    if uninfected[0] > 1:
        ans += uninfected[0] - 1
    else:
        ans = uninfected[0]
    vaccine = 2
    for n in uninfected[1:]:
        n -= vaccine*2
        if n > 0:
            vaccine += 1
            n -= 1
            if n > 1:
                vaccine += 1
                ans += n
            else:
                ans += 1
        else:
            break
    print(N - ans)


T = I()
for ___ in range(T):
    solve()
