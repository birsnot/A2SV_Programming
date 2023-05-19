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
        u, v = II()
        adj[u].append(v)
        adj[v].append(u)
    st = 0
    for ver, edges in adj.items():
        if len(edges) == 1:
            st = ver
            break
    ans = [st]
    v = st
    prev = "a"
    while len(ans) < N + 1:
        for e in adj[v]:
            if e != prev:
                prev = v
                v = e
                break
        ans.append(v)
    print(*ans)
    

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