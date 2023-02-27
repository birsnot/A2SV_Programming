class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mono_stack = []
        greater = {}
        for n in nums2:
            while mono_stack and mono_stack[-1] < n:
                greater[mono_stack.pop()] = n
            mono_stack.append(n)
        for i, n in enumerate(nums1):
            if n in greater:
                nums1[i] = greater[n]
            else:
                nums1[i] = -1
        return nums1