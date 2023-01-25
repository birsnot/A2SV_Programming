class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people)-1
        ans = 0
        while left < right:
            if people[right] + people[left] <= limit:
                ans += 1
                left += 1
                right -= 1
            else:
                ans += 1
                right -= 1
        if left == right:
            ans += 1
        return ans