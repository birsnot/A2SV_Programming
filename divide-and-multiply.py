# author: birsnot - Nardos Wehabe

from sys import stdin
# def input(): return stdin.readline()[:-1]
input = stdin.readline
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))

def fact(n):
    twos = 0
    rem = 0
    while n%2 == 0:
        n //= 2
        twos += 1
    return (twos, n)

def solve():
    N = I()
    nums = IL()
    facts = []
    for n in nums:
        facts.append(fact(n))
    twos = 0
    rems = 0
    for t, r in facts:
        twos += t
        rems += r
    ans = 0
    for i, (t, r) in enumerate(facts):
        n = nums[i]
        cur = n*(1<<(twos - t)) + rems - r
        ans = max(ans, cur)
    print(ans)

T = I()
# T = 1
for ___ in range(T):
    solve()
