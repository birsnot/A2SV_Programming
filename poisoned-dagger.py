# author: birsnot - Nardos Wehabe

def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))


def solve():
    N, H = II()
    hits = IL()

    def check(k):
        total = 0
        prev = -1 - k
        for n in hits:
            total += min((n + k) - (prev + k), k)
            prev = n
        return total >= H
    
    l = 0
    r = H
    while l <= r:
        mid = (l + r)>>1
        if check(mid):
            r = mid - 1
        else:
            l = mid + 1
    print(l)

T = I()
for ___ in range(T):
    solve()
