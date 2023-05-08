# author: birsnot - Nardos Wehabe

from collections import defaultdict, deque
from sys import setrecursionlimit, stdin
# def input(): return stdin.readline()[:-1]
input = stdin.readline
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))
setrecursionlimit(200000)

def solve():
    N, K = II()
    cats = IL()
    adj = defaultdict(list)
    for _ in range(N - 1):
        u, v = II()
        adj[u].append(v)
        adj[v].append(u)

    stack = deque([(1, 0, 0)])
    cnt = 0
    ans = 0
    while stack:
        L = len(stack)
        for i in range(L):
            p, pp, cnt = stack.popleft()
            if cats[p - 1] == 1:
                cnt += 1
                if cnt > K:
                    continue
            else:
                cnt = 0
            if adj[p] == [pp]:
                ans += 1
                continue
            for ch in adj[p]:
                if ch != pp:
                    stack.append((ch, p, cnt))
    print(ans)
    
T = 1
for ___ in range(T):
    solve()
