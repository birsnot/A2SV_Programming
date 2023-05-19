# author: birsnot - Nardos Wehabe


from collections import defaultdict, deque
from sys import setrecursionlimit, stdin
# from threading import Thread, stack_size
# def input(): return stdin.readline()[:-1]
input = stdin.readline
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))

def solve():
    input()
    N, K = II()
    adj = defaultdict(list)
    for _ in range(N - 1):
        u, v = II()
        adj[u].append(v)
        adj[v].append(u)
    dq = deque()
    depths = [0]*(N+1)
    degrees = [0]*(N + 1)
    for v in adj:
        d = len(adj[v])
        degrees[v] = d
        if d == 1:
            dq.append(v)
            degrees[v] -= 1
            depths[v] = 1
    depth = 1
    while dq:
        L = len(dq)
        depth += 1
        for _ in range(L):
            v = dq.popleft()
            for ch in adj[v]:
                if degrees[ch] == 2:
                    depths[ch] = depth
                    dq.append(ch)
                degrees[ch] -= 1
    ans = 0
    for n in depths:
        if n > K:
            ans += 1
    print(ans)

def main():
    T = I()
    # T = 1
    for ___ in range(T):
        solve()

main()

# setrecursionlimit(100050)
# stack_size(1<<27)
# _mt = Thread(target=main)
# _mt.start()
# _mt.join()