# author: birsnot - Nardos Wehabe

def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))


def solve():
    N, M = II()
    remain = IL()
    costs = IL()
    cheaps = [[costs[i], i] for i in range(N)]
    cheaps.sort()
    ptr = 0
    for _ in range(M):
        food, k = II()
        food -= 1
        if remain[food] >= k:
            remain[food] -= k
            print(k*costs[food])
        else:
            cost = remain[food]*costs[food]
            k -= remain[food]
            remain[food] = 0
            while k > 0:
                if ptr >= N:
                    cost = 0
                    break
                if remain[cheaps[ptr][1]] > k:
                    cost += cheaps[ptr][0]*k
                    remain[cheaps[ptr][1]] -= k
                    k = 0
                else:
                    cost += cheaps[ptr][0]*remain[cheaps[ptr][1]]
                    k -= remain[cheaps[ptr][1]]
                    remain[cheaps[ptr][1]] = 0
                    ptr += 1
            print(cost)


T = 1
for ___ in range(T):
    solve()
