# author: birsnot - Nardos 


from collections import deque
from heapq import heapify, heappop, heappush
from sys import setrecursionlimit, stdin
from threading import Thread, stack_size
def input(): return stdin.readline()[:-1]
# input = stdin.readline
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))

def solve():
    N, M, P = II()
    grid = []
    for _ in range(N):
        grid.append(list(input()))
    ps = IL()
    drc = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
    st = 0
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == "M":
                st = (r, c)
                grid[r][c] = "."
                break
        if st: break

    def inbound(r, c):
        return -1 < r < N and -1 < c < M and grid[r][c] != "#"
    def inbound2(r, c):
        return -1 < r < N and -1 < c < M and grid[r][c] == "."
    
    r, c = st
    for j, i in enumerate(ps, 1):
        dr, dc = drc[i]
        nr = r + dr
        nc = c + dc
        if i and inbound(nr, nc):
            r = nr
            c = nc
    dq = deque([(r, c, P)])
    drc.pop(0)
    while dq:
        L = len(dq)
        for _ in range(L):
            r, c, d = dq.popleft()
            if d > 0:
                for dr, dc in drc:
                    nr = r + dr
                    nc = c + dc
                    if inbound2(nr, nc):
                        grid[nr][nc] = "M"
                        dq.append((nr, nc, d - 1))
    ans = 0
    for row in grid:
        ans += row.count("M")
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