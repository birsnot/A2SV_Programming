class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        s = self.score(nums, 0, len(nums)-1, False)
        return s[0] >= s[1]

    def score(self, nums, l, r, turn):
        if l == r:
            ret = [0, 0]
            ret[turn] = nums[l]
            return ret

        left = self.score(nums, l + 1, r, not turn)
        right = self.score(nums, l, r - 1, not turn)
        left[turn] += nums[l]
        right[turn] += nums[r]
        if right[turn] > left[turn]:
            return right
        else:
            return left