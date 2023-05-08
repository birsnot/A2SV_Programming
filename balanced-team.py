N = int(input())
nums = sorted(map(int, input().split()))
i = 0
j = 1
while j < N:
    if nums[j] > nums[i] + 5:
        i += 1
    j += 1
print(j - i)