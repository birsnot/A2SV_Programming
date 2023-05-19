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
    N, X = II()
    favs = IL()
    sum_ = (X*(X + 1))//2
    for n in favs:
        if n <= X:
            sum_ -= 2*n
    print(sum_)
    

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