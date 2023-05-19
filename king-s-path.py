# author: birsnot - Nardos 


from bisect import bisect_right
from collections import defaultdict, deque
from sys import setrecursionlimit, stdin
from threading import Thread, stack_size
# def input(): return stdin.readline()[:-1]
input = stdin.readline
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))

def solve():
    X0, Y0, X1, Y1 = II()
    M = I()
    rows = defaultdict(list)
    for _ in range(M):
        r, a, b = II()
        rows[r].append((a, b))
    for r, cols in rows.items():
        cols.sort()
        tempc = [list(cols[0])]
        for a, b in cols:
            if a <= tempc[-1][1]:
                tempc[-1][1] = max(tempc[-1][1], b)
            else:
                tempc.append([a, b])
        rows[r] = tempc
    drc = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]

    R = C = 1e9 + 1

    visited = set()

    def inbound(r, c):
        if 0 < r < R and 0 < c < C and r in rows and (r, c) not in visited:
            idx = bisect_right(rows[r], [c, C])
            if idx > 0 and rows[r][idx-1][1] >= c:
                return True
        return False
    
    dq = deque([(X0, Y0)])
    ans = 0
    while dq:
        L = len(dq)
        ans += 1
        for _ in range(L):
            r, c = dq.popleft()
            for dr, dc in drc:
                nr = r + dr
                nc = c + dc
                if nr == X1 and nc == Y1:
                    print(ans)
                    return
                if inbound(nr, nc):
                    visited.add((nr, nc))
                    dq.append((nr, nc))
    print(-1)



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