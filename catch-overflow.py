# author: birsnot - Nardos Wehabe

def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))


def solve():
    L = I()
    stk = [[1, 0]]
    for _ in range(L):
        cmd = input()
        if cmd[0] == "a":
            stk[-1][1] += 1
        elif cmd[0] == "f":
            loops = int(cmd.split()[1])
            stk.append([loops, 0])
        else:
            loops, n = stk.pop()
            stk[-1][1] += loops*n
    while len(stk) > 1:
        loops, n = stk.pop()
        stk[-1][1] += loops*n
    ans = stk[0][0]*stk[0][1]
    if ans > (2**32 - 1):
        print("OVERFLOW!!!")
    else:
        print(ans)


T = 1
for ___ in range(T):
    solve()
