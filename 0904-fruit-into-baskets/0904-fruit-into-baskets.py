class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        my_fruits = defaultdict(int)
        l = 0
        for fr in fruits:
            my_fruits[fr] += 1
            if len(my_fruits) > 2:
                if my_fruits[fruits[l]] == 1:
                    del my_fruits[fruits[l]]
                else:
                    my_fruits[fruits[l]] -= 1
                l += 1
        return len(fruits) - l