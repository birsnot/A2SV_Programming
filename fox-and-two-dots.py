# author: birsnot - Nardos 


from sys import setrecursionlimit, stdin
from threading import Thread, stack_size
def input(): return stdin.readline()[:-1]
# input = stdin.readline
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))

def solve():
    N, M = II()
    grid = []
    for _ in range(N):
        grid.append(input())
    
    visited = set()
    drc = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def inbound(r, c, clr):
        return -1 < r < N and -1 < c < M and grid[r][c] == clr

    def dfs(r, c, clr, pr, pc):
        visited.add((r, c))
        for dr, dc in drc:
            nr = r + dr
            nc = c + dc
            if nr == pr and nc ==  pc:
                continue
            if inbound(nr, nc, clr):
                if (nr, nc) not in visited:
                    if dfs(nr, nc, clr, r, c):
                        return True
                else:
                    return True
        return False
    for r in range(N):
        for c in range(M):
            if (r, c) not in visited:
                if dfs(r, c, grid[r][c], -1, -1):
                    print("Yes")
                    return
    print("No")

def main():
    # T = I()
    T = 1
    for ___ in range(T):
        solve()

# main()

setrecursionlimit(4000)
stack_size(1000000)
_mt = Thread(target=main)
_mt.start()
_mt.join()