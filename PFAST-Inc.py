# author: birsnot - Nardos Wehabe


from sys import setrecursionlimit, stdin
# from threading import Thread, stack_size
def input(): return stdin.readline()[:-1]
# input = stdin.readline
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))

def solve():
    N, M = II()
    names = []
    names_i = {}
    for i in range(N):
        s = input()
        names.append(s)
        names_i[s] = i

    edges = set()
    for _ in range(M):
        edges.add(tuple(input().split()))
    
    cur = set()
    ans = set()
    visited = set()

    def bt(mask):
        nonlocal ans, cur
        if len(cur) > len(ans):
            ans = cur.copy()
        for i in range(N):
            p = 1<<names_i[names[i]]
            if p&mask == 0:
                found = False
                for name in cur:
                    if (name, names[i]) in edges or (names[i], name) in edges:
                        found = True
                        break
                mask |= p
                if not found and mask not in visited:
                    cur.add(names[i])
                    visited.add(mask)
                    bt(mask)
                    cur.remove(names[i])
                mask ^= p
    bt(0)
    print(len(ans))
    print(*sorted(ans), sep="\n")

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