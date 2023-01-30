T = int(input())
for _ in range(T):
    n, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    check = []
    prev = nums[0]
    for num in nums:
        check.append(prev/num)
        prev = num
    left = 0
    right = 0
    ans = 0
    while right < n-1:
        right += 1
        if check[right] >= 2:
            left = right
        if right - left == k:
            ans += 1
            left += 1
    print(ans)
