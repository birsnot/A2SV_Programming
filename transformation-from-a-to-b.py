# author: birsnot - Nardos Wehabe

from collections import deque
from sys import setrecursionlimit, stdin
# def input(): return stdin.readline()[:-1]
input = stdin.readline
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))
setrecursionlimit(100000)

def solve():
    A, B = II()
    a = A
    b = B
    ans = deque()
    ans.appendleft(B)
    while a <= b:
        if a == b:
            print("YES")
            print(len(ans))
            print(*ans)
            return
        mod = b%10
        if mod == 1:
            b //= 10
            ans.appendleft(b)
        elif mod%2 == 0:
            b //= 2
            ans.appendleft(b)
        else:
            print("NO")
            return
    print("NO")


# T = I()
T = 1
for ___ in range(T):
    solve()
