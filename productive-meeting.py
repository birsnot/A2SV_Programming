# author: birsnot - Nardos 


from heapq import heapify, heappop, heappush
from sys import setrecursionlimit, stdin
from threading import Thread, stack_size
# def input(): return stdin.readline()[:-1]
input = stdin.readline
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))

def solve():
    N = I()
    nums = IL()
    pq = []
    for i, n in enumerate(nums, 1):
        if n:
            pq.append((-n, i))
    heapify(pq)
    ans = []
    while len(pq) > 1:
        a1, i1 = heappop(pq)
        a2, i2 = heappop(pq)
        ans.append((i1, i2))
        if a1 < -1:
            heappush(pq, (a1 + 1, i1))
        if a2 < -1:
            heappush(pq, (a2 + 1, i2))
    print(len(ans))
    for a in ans:
        print(*a)

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