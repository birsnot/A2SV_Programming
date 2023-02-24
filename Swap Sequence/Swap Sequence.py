N = int(input())
ans = []
nums = list(map(int, input().split()))
for i, n in enumerate(nums):
    min_ = n
    idx = j = i
    while j < N:
        if nums[j] < min_:
            min_ = nums[j]
            idx = j
        j += 1
    nums[i], nums[idx] = nums[idx], nums[i]
    ans.append((i, idx))
print(len(ans))
for a in ans:
    print(*a)
