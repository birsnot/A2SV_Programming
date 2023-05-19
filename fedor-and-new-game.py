# author: birsnot - Nardos 


from sys import setrecursionlimit, stdin
from threading import Thread, stack_size
# def input(): return stdin.readline()[:-1]
input = stdin.readline
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))

def count(n):
    cnt = 0
    while n > 0:
        cnt += n&1
        n >>= 1
    return cnt

def solve():
    N, M, K = II()
    armys = []
    for _ in range(M):
        armys.append(I())
    fedor = I()
    ans = 0
    for army in armys:
        diff = army^fedor
        if count(diff) <= K:
            ans += 1
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