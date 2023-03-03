class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mono_stk = [(0, 1)]
        sum_ = ans = 0
        for n in arr:
            sum_ += n
            count = 1
            while mono_stk[-1][0] > n:
                m, c = mono_stk.pop()
                count += c
                sum_ += (n - m)*c
            ans += sum_
            mono_stk.append((n, count))
        return ans%1000000007