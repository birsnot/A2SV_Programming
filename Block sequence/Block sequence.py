N, M = map(int, input().split())
nums = sorted(map(int, input().split()))
ans = 0
buffer = nums[0] - 1
for i, n in enumerate(nums[1:]):
    ans += min(nums[i], n - 1)
    if nums[i] == n and buffer:
        ans += 1
        buffer -= 1
    elif n > nums[i]+1:
        buffer += n - nums[i] - 1
print(ans)
