class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        chalks = sum(chalk)
        k %= chalks
        for i, n in enumerate(chalk):
            k -= n
            if k < 0: return i
