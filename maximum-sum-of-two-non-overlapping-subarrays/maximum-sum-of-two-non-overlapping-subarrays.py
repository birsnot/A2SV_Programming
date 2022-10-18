class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        ps = [0]
        temp = 0
        for n in nums:
            temp += n
            ps.append(temp)

        j1 = firstLen
        i1 = 0
        total = 0
        while j1 < len(ps):
            sum1 = ps[j1] - ps[i1]
            j2 = secondLen
            i2 = 0
            while j2 < len(ps):
                if i1 < j2 <= j1 or i1 <= i2 < j1 or i2 < j1 <= j2 or i2 <= i1 < j2:
                    j2 = j1 + secondLen
                    i2 = j1
                else:
                    sum2 = ps[j2] - ps[i2]
                    total = max(total, sum1 + sum2)
                    j2 += 1
                    i2 += 1
            j1 += 1
            i1 += 1

        return total
