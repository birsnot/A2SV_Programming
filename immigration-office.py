# author: birsnot - Nardos Wehabe

def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))


def bisect_left(names, name):
    l = 0
    r = len(names) - 1
    while l <= r:
        mid = (r + l)//2
        if names[mid] < name:
            l = mid + 1
        else:
            r = mid - 1
    return l


def solve():
    N = I()
    names = list(input().split())
    Q = I()
    for _ in range(Q):
        name = input()
        print(bisect_left(names, name))


T = 1
for ___ in range(T):
    solve()
