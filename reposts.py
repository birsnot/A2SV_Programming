# author: birsnot - Nardos 


from collections import defaultdict
from sys import setrecursionlimit, stdin
from threading import Thread, stack_size
def input(): return stdin.readline()[:-1]
# input = stdin.readline
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))

def lw(s):
    return s.lower()

def solve():
    N = I()
    child = defaultdict(list)
    for _ in range(N):
        ch, _ , p = map(lw, input().split())
        child[p].append(ch)
    def dfs(v):
        ret = 0
        for ch in child[v]:
            ret = max(ret, dfs(ch))
        return ret + 1

    print(dfs("polycarp"))

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