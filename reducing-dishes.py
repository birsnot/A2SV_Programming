class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        sum_ = ans = 0
        for n in satisfaction:
            sum_ += n
            if sum_ <= 0:
                return ans
            ans += sum_
        return ans