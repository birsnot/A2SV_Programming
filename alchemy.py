# author: birsnot - Nardos Wehabe

def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))


def solve():
    N = I()
    ingredients = IL()
    edward_count = 0
    edward_sum = 0
    alphonse_count = 0
    alphonse_sum = 0
    l = 0
    r = N - 1
    while l <= r:
        if alphonse_sum < edward_sum:
            alphonse_sum += ingredients[r]
            alphonse_count += 1
            r -= 1
        else:
            edward_sum += ingredients[l]
            edward_count += 1
            l += 1
    print(edward_count, alphonse_count)

T = 1
for ___ in range(T):
    solve()
