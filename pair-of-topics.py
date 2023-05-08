N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
nums = [0]*N
for i, (ai, bi) in enumerate(zip(a, b)):
    nums[i] = ai - bi
nums.sort()
j = N - 1
prev = 0
ans = 0
for i, n in enumerate(nums):
    temp = prev
    if i > j:
        temp -= 1
    while j > i:
        if n > -nums[j]:
            temp += 1
            j -= 1
        else:
            break
    prev = temp
    ans += temp
print(ans)