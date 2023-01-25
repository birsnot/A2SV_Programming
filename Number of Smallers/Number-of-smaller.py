n1, n2 = map(int, input().split())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
ans = []
count = 0
pt = 0
for num in nums2:
    while pt < n1 and num > nums1[pt]:
        count += 1
        pt += 1
    ans.append(count)
print(*ans)
