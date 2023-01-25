class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        skill_sum = skill[0] + skill[-1]
        left = 0
        right = len(skill)-1
        ans = 0
        while left < right:
            if skill[left] + skill[right] == skill_sum:
                ans += skill[left]*skill[right]
            else:
                return -1
            left += 1
            right -= 1
        return ans