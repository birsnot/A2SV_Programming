# author: birsnot - Nardos Wehabe


from collections import deque
from sys import setrecursionlimit, stdin
# from threading import Thread, stack_size
def input(): return stdin.readline()[:-1]
# input = stdin.readline
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))

def solve():
    n = input()
    m = input()
    if n == "0":
        ans = "0"
    else:
        n = sorted(n)
        for i, d in enumerate(n):
            if d != "0":
                break
        d = n.pop(i)
        n.insert(0, d)
        ans = "".join(n)
    if ans == m:
        print("OK")
    else:
        print("WRONG_ANSWER")
    

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