class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        num_q = deque()
        i = 0
        arr_len = len(arr)
        while i < arr_len:
            num_q.append(arr[i])
            if arr[i] == 0:
                num_q.append(0)
            arr[i] = num_q.popleft()
            i += 1