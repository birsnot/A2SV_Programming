class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        arr_len = len(arr)
        if arr_len < 3: return False
        i = 1
        while i < arr_len and arr[i - 1] < arr[i]:
            i += 1
        if i == arr_len or i == 1: return False
        while i < arr_len and arr[i - 1] > arr[i]:
            i += 1
        if i != arr_len: return False
        return True