class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []
        Len = len(nums)
        def bt(mask):
            for i in range(Len):
                if mask&(1<<i) == 0:
                    cur.append(nums[i])
                    if len(cur) == Len:
                        ans.append(cur.copy())
                        cur.pop()
                        return
                    bt(mask|(1<<i))
                    cur.pop()
        bt(0)
        return ans