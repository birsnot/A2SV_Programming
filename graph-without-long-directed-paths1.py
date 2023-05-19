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
    N, M = II()
    frm = defaultdict(list)
    to = defaultdict(list)
    for i in range(M):
        u, v = II()
        to[u].append((v, i))
        frm[v].append((u, i))
    ans = [0]*M
    visited = {}
    source = 1
    sink = 2
    def dfs(u, prev):
        visited[u] = cur = prev^3
        for v, i in to[u]:
            ans[i] = [1, 0][cur == source]
            if v not in visited:
                if not dfs(v, cur):
                    return False
            elif visited[v] != prev:
                return False
        for v, i in frm[u]:
            ans[i] = [1, 0][cur == sink]
            if v not in visited:
                if not dfs(v, cur):
                    return False
            elif visited[v] != prev:
                return False
        return True
    
    if dfs(1, 1):
        print("YES")
        print(*ans, sep="")
    else:
        print("NO")

    

def main():
    # T = I()
    T = 1
    for ___ in range(T):
        solve()

# main()

setrecursionlimit(300500)
stack_size(100000000)
_mt = Thread(target=main)
_mt.start()
_mt.join()