N = int(input())
boys = sorted(map(int, input().split()))
M = int(input())
girls = sorted(map(int, input().split()))
b = g = 0
ans = 0
while b < N and g < M:
    dif = abs(boys[b] - girls[g])
    if dif > 1:
        if boys[b] > girls[g]:
            g += 1
        else:
            b += 1
    else:
        ans += 1
        g += 1
        b += 1
print(ans)