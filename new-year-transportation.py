# author: birsnot - Nardos 


from sys import setrecursionlimit, stdin
from threading import Thread, stack_size
# def input(): return stdin.readline()[:-1]
input = stdin.readline
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))

def solve():
    N, T = II()
    portals = IL()
    portals.append(0)
    nxt = 1 + portals[0]
    visited = set()
    visited.add(1)
    while nxt != T:
        if nxt in visited:
            break
        visited.add(nxt)
        nxt = nxt + portals[nxt - 1]
    if nxt == T:
        print("YES")
    else:
        print("NO")
    

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