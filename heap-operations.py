# author: birsnot - Nardos 


from heapq import heappop, heappush
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
    inp = []
    for _ in range(N):
        opr = input()
        if opr[0] == 'r':
            inp.append((opr, ""))
        else:
            opr, n = opr.split()
            inp.append((opr, int(n)))
    ans = []
    pq = []
    for opr in inp:
        if opr[0][0] == "r":
            if not pq:
                ans.append(("insert", 1))
                ans.append(opr)
            else:
                heappop(pq)
                ans.append(opr)
        elif opr[0][0] == "i":
            heappush(pq, opr[1])
            ans.append(opr)
        else:
            while pq and pq[0] < opr[1]:
                heappop(pq)
                ans.append(("removeMin", ""))
            if not pq or pq[0] > opr[1]:
                ans.append(("insert", opr[1]))
                heappush(pq, opr[1])
                ans.append(opr)
            else:
                ans.append(opr)
    print(len(ans))
    for a in ans:
        print(*a)
    

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