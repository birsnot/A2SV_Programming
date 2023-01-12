class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        for col in zip(*strs):
            for ch1, ch2 in zip(col,col[1:]):
                if ch1 > ch2:
                    ans += 1
                    break
        return ans