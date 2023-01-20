n = int(input())
nums = list(map(int, input().split()))
even = False
odd = False
for num in nums:
    if num%2:
        odd = True
    else:
        even = True
    if even and odd:
        break

if even and odd:
    print(*sorted(nums))
else:
    print(*nums)
