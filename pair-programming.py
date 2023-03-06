# author: birsnot - Nardos Wehabe

def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))


def solve():
    N, K = II()
    nums = SIL()
    n = 2**(N-1)
    ans = 0
    i = n - 1
    k = K
    while k > n:
        ans += nums[i]*n
        k -= n
        n //= 2
        i += n
    ans += nums[i]*k
    print(ans)


T = 1
for ___ in range(T):
    solve()
