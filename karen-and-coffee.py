# author: birsnot - Nardos Wehabe

def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))


def solve():
    N, K, Q = II()
    counts = [0]*(200002)
    for _ in range(N):
        l, r = II()
        counts[l] += 1
        counts[r+1] -= 1
    prev = 0
    for i in range(1, 200002):
        count = counts[i] + prev
        counts[i] = counts[i-1] + (count >= K)
        prev = count
    for __ in range(Q):
        l, r = II()
        print(counts[r]-counts[l-1])


T = 1
for ___ in range(T):
    solve()
