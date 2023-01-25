class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        c = [0]*30001
        for weight in people:
            c[weight] += 1
        ans = sum(c[limit:])
        left = 1
        right = limit-1
        while left < right:
            if not c[right]:
                right -= 1
            elif not c[left]:
                left += 1
            elif left + right > limit:
                ans += 1
                c[right] -= 1
            else:
                ans += 1
                c[left] -= 1
                c[right] -= 1
        if left*2 <= limit:
            ans += ceil(c[left]/2)
        else:
            ans += c[left]
        return ans