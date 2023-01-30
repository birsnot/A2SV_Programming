N = int(input())
nums = list(map(int, input().split()))
wube = 0
henok = 0
left = 0
right = N - 1
flag = True
while left <= right:
    if flag:
        if nums[left] > nums[right]:
            wube += nums[left]
            left += 1
        else:
            wube += nums[right]
            right -= 1
        flag = False
    else:
        if nums[left] > nums[right]:
            henok += nums[left]
            left += 1
        else:
            henok += nums[right]
            right -= 1
        flag = True
print(wube, henok)
