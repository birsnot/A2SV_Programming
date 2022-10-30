class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        half = len(arr)//2
        c = Counter(arr).most_common()
        removed = ans = 0
        for _,fr in c:
            ans += 1
            removed += fr
            if removed >= half:
                return ans
