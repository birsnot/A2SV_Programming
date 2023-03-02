class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        for i in range(k):
            tickets[i] -= 1
        n = tickets[k]
        ans = k + n
        n -= 1
        tickets[k] = 0
        for m in tickets:
            ans += min(n, m)
        return ans