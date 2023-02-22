class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ps = [0] + list(accumulate(nums))
        sum_ = ps[-1]
        # ps.append(sum_)
        for i in range(len(nums)):
            if ps[i] == sum_ - ps[i+1]:
                return i
        return -1