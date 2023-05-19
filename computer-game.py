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
    N = I()
    grid = []
    for _ in range(2):
        grid.append(list(input()))
    def inbound(r, c):
        return -1 < r < 2 and -1 < c < N
    drc = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
    def dfs(r, c):
        if r == 1 and c == N - 1:
            return True
        grid[r][c] = '1'
        for dr, dc in drc:
            nr = r + dr
            nc = c + dc
            if inbound(nr, nc) and grid[nr][nc] == "0":
                if dfs(nr, nc):
                    return True
        return False
    if dfs(0, 0):
        print("YES")
    else:
        print("NO")

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