class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = 0
        def merge(l, r):
            if l == r:
                return [nums[l]]
            mid = (l + r)>>1
            left = merge(l, mid)
            right = merge(mid + 1, r)
            nonlocal ans
            prev = p = 0
            for n in left:
                cur = prev
                k = (n + 1)//2
                while p < len(right) and right[p] < k:
                    cur += 1
                    p += 1
                ans += cur
                prev = cur
            ret = []
            p1 = p2 = 0
            while p1 < len(left) and p2 < len(right):
                if left[p1] <= right[p2]:
                    ret.append(left[p1])
                    p1 += 1
                else:
                    ret.append(right[p2])
                    p2 += 1
            ret.extend(left[p1:])
            ret.extend(right[p2:])
            return ret
        merge(0, len(nums) - 1)
        return ans