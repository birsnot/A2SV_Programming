T = int(input())
for _ in range(T):
    size = int(input())
    nums = list(map(int, input().split()))
    positive = nums[0] > 0
    ans = 0
    max_ = float("-inf")
    for n in nums:
        if positive:
            if n > 0:
                max_ = max(max_, n)
            else:
                positive = False
                ans += max_
                max_ = n
        else:
            if n < 0:
                max_ = max(max_, n)
            else:
                positive = True
                ans += max_
                max_ = n
    ans += max_
    print(ans)
