n = int(input())
nums = sorted(map(int, input().split()))
nums[-1], nums[-2] = nums[-2], nums[-1]
if nums[-3] + nums[-1] > nums[-2]:
    print("YES")
    print(*nums)
else:
    print("NO")
