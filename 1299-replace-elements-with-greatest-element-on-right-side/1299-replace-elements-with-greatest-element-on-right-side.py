class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_ = -1
        arr_len = len(arr)
        for i in range(arr_len - 1, -1, -1):
            val = arr[i]
            arr[i] = max_
            if val > max_:
                max_ = val
        return arr