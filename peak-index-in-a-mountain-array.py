class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 1
        r = len(arr) - 2
        while l <= r:
            mid = (l + r)//2
            if arr[mid - 1] < arr[mid]:
                if arr[mid] < arr[mid + 1]:
                    l = mid + 1
                else:
                    return mid
            else:
                r = mid - 1