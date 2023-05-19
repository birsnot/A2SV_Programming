# author: birsnot - Nardos 


from collections import defaultdict
from sys import setrecursionlimit, stdin
from threading import Thread, stack_size
# def input(): return stdin.readline()[:-1]
input = stdin.readline
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))

def solve():
    N = I()
    adj = defaultdict(list)
    for _ in range(N):
        u, v, c = II()
        adj[u].append((v, 0))
        adj[v].append((u, c))

    def dfs(u, p):
        if u == 1:
            return 0
        ret = 0
        for v, c in adj[u]:
            if v != p:
                ret += c + dfs(v, u)
        return ret

    ans = float('inf')
    for v, c in adj[1]:
        cur = c
        cur += dfs(v, 1)
        ans = min(ans, cur)
    print(ans)
    

def main():
    # T = I()
    T = 1
    for ___ in range(T):
        solve()

main()

# setrecursionlimit(100050)
# stack_size(1<<27)
# _mt = Thread(target=main)
# _mt.start()
# _mt.join()