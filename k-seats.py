N, M, K = map(int, input().split())
seats = []
for _ in range(N):
    seats.append(input())
ans = 0
for row in seats:
    count = 0
    for ch in row:
        if ch == ".":
            count += 1
            if count == K:
                ans += 1
                count -= 1
        else:
            count = 0
if K != 1:
    for row in zip(*seats):
        count = 0
        for ch in row:
            if ch == ".":
                count += 1
                if count == K:
                    ans += 1
                    count -= 1
            else:
                count = 0
print(ans)