class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        neg = [1, -nums[0]]
        pos = [1, nums[0]]
        for n in nums:
            if -neg[1] < n:
                cur_pos = [neg[0] + 1, n]
                pos = max(cur_pos, pos)
            if pos[1] > n:
                cur_neg = [pos[0] + 1, -n]
                neg = max(cur_neg, neg)
        return max(neg[0], pos[0])