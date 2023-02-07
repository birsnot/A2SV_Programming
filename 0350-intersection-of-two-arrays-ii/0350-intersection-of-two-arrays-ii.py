class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        N1 = len(nums1)
        N2 = len(nums2)
        p1 = p2 = 0
        nums1.sort()
        nums2.sort()
        while p1 < N1 and p2 < N2:
            if nums1[p1] == nums2[p2]:
                ans.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                p1 += 1
        return ans