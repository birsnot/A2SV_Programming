class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        c = -1
        while i > -1 and j > -1:
            if nums1[i] > nums2[j]:
                nums1[c] = nums1[i]
                i -= 1
            else:
                nums1[c] = nums2[j]
                j -= 1
            c -= 1
        while j > -1:
            nums1[c] = nums2[j]
            j -= 1
            c -= 1
        