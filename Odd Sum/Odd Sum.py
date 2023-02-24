N = int(input())
nums = sorted(map(int, input().split()))
if nums[0] == nums[-1]:
    print(-1)
else:
    print(*nums)
