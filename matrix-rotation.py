def check(row1, row2):
    if row1[0] < row1[1] and row2[0] < row2[1] and row1[0] < row2[0] and row1[1] < row2[1]:
        return True
    return False

def rotate(row1, row2):
    r1 = [row2[0], row1[0]]
    r2 = [row2[1], row1[1]]
    return [r1, r2]

T = int(input())
for _ in range(T):
    row1 = list(map(int, input().split()))
    row2 = list(map(int, input().split()))
    ans = check(row1, row2)
    if ans:
        print("YES")
        continue
    row1, row2 = rotate(row1, row2)
    ans = check(row1, row2)
    if ans:
        print("YES")
        continue
    row1, row2 = rotate(row1, row2)
    ans = check(row1, row2)
    if ans:
        print("YES")
        continue
    row1, row2 = rotate(row1, row2)
    ans = check(row1, row2)
    if ans:
        print("YES")
        continue
    print("NO")