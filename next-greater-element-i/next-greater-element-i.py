class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def nxt(n):
            k = nums2.index(n)
            for i in range(k + 1, len(nums2)):
                if nums2[i] > nums2[k]:
                    return nums2[i]
            return -1
        ans = [0]*len(nums1)
        for i,n in enumerate(nums1):
            ans[i] = nxt(n)
        return ans
