class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for a,b in zip(l,r):
            sub = sorted(nums[a:b+1])
            d = sub[1] - sub[0]
            st = True
            j = 2
            while  j < len(sub):
                if sub[j] - sub[j-1] != d:
                    st = False
                    break
                j += 1
            ans.append(st)
        return ans
