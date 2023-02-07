class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit = [-1, -1, -1, -1]
        N = len(fruits)
        l = r = 0
        while r < N and -1 in fruit:
            if fruits[r] == fruit[0]:
                fruit[1] = r
            elif fruit[0] == -1:
                fruit[0] = fruits[r]
                fruit[1] = r
            else:
                fruit[2] = fruits[r]
                fruit[3] = r
            r += 1
        ans = r - l        
        while r < N:
            if fruits[r] == fruit[0]:
                fruit[1] = r
            elif fruits[r] == fruit[2]:
                fruit[3] = r
            else:
                if fruit[1] < fruit[3]:
                    l = fruit[1] + 1
                    fruit[0] = fruits[r]
                    fruit[1] = r
                else:
                    l = fruit[3] + 1
                    fruit[2] = fruits[r]
                    fruit[3] = r
            r += 1
            ans = max(ans, r - l)
        return ans