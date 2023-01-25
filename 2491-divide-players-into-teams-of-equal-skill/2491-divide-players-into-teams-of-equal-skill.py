class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        c = Counter(skill)
        skill_sum = sum(skill)//(len(skill)//2)
        ans = 0
        for val, count in c.items():
            pair_skill = skill_sum - val
            if c[pair_skill] != count:
                return -1
            else:
                ans += count*val*pair_skill
        return ans//2