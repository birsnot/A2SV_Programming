len1, len2 = map(int, input().split())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

ans = [0]*(len1+len2)
p1 = 0
p2 = 0
cur = 0
while p1 < len1 and p2 < len2:
    if nums1[p1] < nums2[p2]:
        ans[cur] = nums1[p1]
        p1 += 1
    else:
        ans[cur] = nums2[p2]
        p2 += 1
    cur += 1

while p1 < len1:
    ans[cur] = nums1[p1]
    p1 += 1
    cur += 1

while p2 < len2:
    ans[cur] = nums2[p2]
    p2 += 1
    cur += 1

print(*ans)
