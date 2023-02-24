N = int(input())
nums = list(map(int, input().split()))
neg = []
zeros = 0
pos = []
for n in nums:
    if n == 0:
        zeros += 1
    elif n > 0:
        pos.append(n)
    else:
        neg.append(-n)
ans = sum(pos) - len(pos) + zeros + sum(neg) - len(neg)
if len(neg)%2 and not zeros:
    ans += 2
print(ans)
