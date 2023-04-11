class Solution:
    def createSortedArray(self, ins: List[int]) -> int:
        mn = [0]*len(ins)
        mx = [0]*len(ins)
        def merge(l, r):
            if l == r:
                return [l]
            mid = (l + r)>>1
            left = merge(l, mid)
            right = merge(mid + 1, r)
            equal = prev = prev_n = p = 0
            L = len(left)
            for i in right:
                n = ins[i]
                if n > prev_n:
                    cur = prev + equal
                    equal = 0
                    prev_n = n
                else:
                    mn[i] += prev
                    mx[i] += L - equal - prev
                    continue
                while p < L:
                    if ins[left[p]] < n:
                        cur += 1
                        p += 1
                    elif ins[left[p]] > n:
                        break
                    else:
                        while p < L and ins[left[p]] == n:
                            equal += 1
                            p += 1
                mn[i] += cur
                mx[i] += L - equal - cur
                prev = cur
            ret = []
            p1 = p2 = 0
            R = len(right)
            while p1 < L and p2 < R:
                if ins[left[p1]] <= ins[right[p2]]:
                    ret.append(left[p1])
                    p1 += 1
                else:
                    ret.append(right[p2])
                    p2 += 1
            ret.extend(left[p1:])
            ret.extend(right[p2:])
            return ret
        merge(0, len(ins) - 1)
        ans = 0
        for c in zip(mn, mx):
            ans += min(c)
        return ans%1000_000_007