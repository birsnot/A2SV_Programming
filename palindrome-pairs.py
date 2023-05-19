# author: birsnot - Nardos 


from collections import Counter
from sys import setrecursionlimit, stdin
from threading import Thread, stack_size
def input(): return stdin.readline()[:-1]
# input = stdin.readline
def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))

def solve():
    pos = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    N = I()
    masks = {}
    ans = 0
    for _ in range(N):
        cnt = Counter(input())
        mask = 0
        for ch in cnt:
            mask |= (cnt[ch]%2)<<pos[ch]
        for i in range(26):
            check = mask^(1<<i)
            if check in masks:
                ans += masks[check]
        if mask in masks:
            ans += masks[mask]
            masks[mask] += 1
        else:
            masks[mask] = 1
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