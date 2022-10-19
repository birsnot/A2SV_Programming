class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ps = {0:1}
        temp = 0
        for n in nums:
            temp += n%2
            ps[temp] = ps.get(temp,0)+1
        if k > temp:
            return 0
        temp -= k - 1
        ans = 0
        for i in range(temp):
            ans += ps[i] * ps[k+i]
        return ans
