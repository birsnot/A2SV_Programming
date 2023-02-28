class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        pre = [1]
        temp = 0
        for n in nums:
            temp += n%2
            if len(pre) > temp:
                pre[-1] += 1
            else:
                pre.append(1)
        ans = 0
        loop = len(pre) - k
        for i in range(loop):
            ans += pre[i]*pre[k+i]
        return ans