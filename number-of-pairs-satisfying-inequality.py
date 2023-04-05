class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        N = len(nums1)
        nums = [0]*N
        for i in range(N):
            nums[i] = nums1[i] - nums2[i]
        ans = 0
        def helper(l, r):
            nonlocal ans
            if l == r: return [nums[l]]
            mid = (l + r)//2
            left = helper(l, mid)
            right = helper(mid + 1, r)
            i = 0
            N1 = len(left)
            N2 = len(right)
            ans_ = 0
            prev = 0
            for n in left:
                cur = prev
                num = n - diff
                while i < N2 and right[i] >= num:
                    cur += 1
                    i += 1
                ans_ += cur
                prev = cur
            ans += ans_
            ret = []
            p1 = p2 = 0
            while p1 < N1 and p2 < N2:
                if left[p1] >= right[p2]:
                    ret.append(left[p1])
                    p1 += 1
                else:
                    ret.append(right[p2])
                    p2 += 1
            ret.extend(left[p1:])
            ret.extend(right[p2:])
            return ret
        helper(0, N - 1)
        return ans