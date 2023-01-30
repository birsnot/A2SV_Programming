n = int(input())
nums = list(map(int, input().split()))
check = sorted(nums)
first = 0
second = 0
found1 = False
found2 = False
j = 1
while j < n:
    if not found1:
        if nums[j - 1] > nums[j]:
            first = j
            found1 = True
    else:
        if nums[j - 1] < nums[j]:
            second = j
            found2 = True
    if found1 and found2:
        break
    j += 1

if not found1:
    first = 1
    second = 1
elif not found2:
    second = n
nums = nums[:first - 1] + nums[first - 1:second][::-1] + nums[second:]
if nums == check:
    print("yes")
    print(first, second)
else:
    print("no")
