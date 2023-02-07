class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit = defaultdict(int)
        N = len(fruits)
        l = r = 0
        while r < N and len(fruit) < 2:
            fruit[fruits[r]] = r
            r += 1
        ans = r - l
        while r < N:
            if fruits[r] in fruit:
                fruit[fruits[r]] = r
            else:
                fruit[fruits[r]] = r
                ptr = iter(fruit)
                fr1 = next(ptr)
                fr2 = next(ptr)
                if fruit[fr1] < fruit[fr2]:
                    l = fruit[fr1] + 1
                    del fruit[fr1]
                else:
                    l = fruit[fr2] + 1
                    del fruit[fr2]
            r += 1
            ans = max(ans, r - l)
        return ans