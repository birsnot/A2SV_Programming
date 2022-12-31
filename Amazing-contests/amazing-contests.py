_ = int(input())
scores = list(map(int,input().split()))
ans = 0
max = scores[0]
min = scores[0]
for score in scores:
    if score > max:
        ans += 1
        max = score
    elif score < min:
        ans += 1
        min = score
print(ans)
