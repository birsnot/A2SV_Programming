from collections import deque


T = int(input())
for _ in range(T):
    N = int(input())
    nums = deque(map(int, input().split()))
    ans = []
    while nums:
        ans.append(nums.popleft())
        if nums:
            ans.append(nums.pop())
    print(*ans)
