# author: birsnot - Nardos Wehabe

def I(): return int(input())
def II(): return map(int, input().split())
def IL(): return list(map(int, input().split()))
def SIL(): return sorted(map(int, input().split()))


def solve():
    walk_speed, elev_speed, elev_pos = II()
    def helper(remain, elev_pos, pos):
        if remain == 1:
            return min(walk_speed, (abs(elev_pos - pos)+1)*elev_speed)
        remain -= 1
        elev = helper(remain, pos, pos) + (abs(elev_pos-pos) + 1)*elev_speed
        pos += 1
        walk = helper(remain, elev_pos, pos) + walk_speed
        return min(elev, walk)
    print(helper(4, elev_pos, 0))


T = I()
for ___ in range(T):
    solve()
