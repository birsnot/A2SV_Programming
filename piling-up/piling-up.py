# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for _ in range(T):
    j = int(input()) - 1
    nums = list(map(int, input().split()))
    i = 0
    last = float('inf')
    ans = 'Yes'
    while i <= j:
        if nums[j] > nums[i]:
            if nums[j] > last:
                ans = 'No'
                break
            else:
                last = nums[j]
                j -= 1
        elif nums[i] < nums[j]:
            if nums[i] > last:
                ans = 'No'
                break
            else:
                last = nums[i]
                i += 1
        else:
            if nums[i] > last:
                ans = 'No'    
                break
            else:
                last = nums[i]
                i += 1
                j -= 1
    print(ans)
