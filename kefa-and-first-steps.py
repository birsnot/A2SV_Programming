N = int(input())
nums = list(map(int, input().split()))
count = 1
ans = 1
for i, n in enumerate(nums[1:]):
    if nums[i] > n:
        ans = max(count, ans)
        count = 1
    else:
        count += 1
ans = max(count, ans)
print(ans)