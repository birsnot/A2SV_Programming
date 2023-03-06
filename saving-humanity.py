# author: birsnot - Nardos Wehabe

def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))


def solve():
    N, M = II()
    state = list(input())
    for j in range(M):
        new_state = [""]*N
        if state[1] == "1":
            new_state[0] = "1"
        else:
            new_state[0] = state[0]
        for i, n in enumerate(state[1:-1], 1):
            if (state[i-1] == "0" and state[i+1] == "1") or (state[i-1] == "1" and state[i+1] == "0"):
                new_state[i] = "1"
            else:
                new_state[i] = n
        if state[-2] == "1":
            new_state[-1] = "1"
        else:
            new_state[-1] = state[-1]
        if new_state == state:
             break
        state = new_state
    print("".join(state))

T = I()
for ___ in range(T):
    solve()
