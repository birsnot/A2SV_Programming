class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        def merge(l, r):
            if l == r:
                return [l]
            mid = (l + r)>>1
            left = merge(l, mid)
            right = merge(mid + 1, r)
            prev = p = 0
            for i in left:
                cur = prev
                while p < len(right) and nums[right[p]] < nums[i]:
                    cur += 1
                    p += 1
                ans[i] += cur
                prev = cur
            ret, p1, p2 = [], 0, 0
            while p1 < len(left) and p2 < len(right):
                if nums[left[p1]] <= nums[right[p2]]:
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