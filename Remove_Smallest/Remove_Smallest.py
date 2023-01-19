T = int(input())
for _ in range(T):
    n = int(input())
    nums = sorted(map(int, input().split()))
    ans = "YES"
    for i in range(1, n):
        if nums[i] - nums[i - 1] > 1:
            ans = "NO"
            break
    print(ans)
