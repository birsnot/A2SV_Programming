class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        f1 = f2 = -1
        last_seen = [-1, -1]
        i = ans = count = 0
        for j in range(len(fruits)):
            if fruits[j] == f1 or fruits[j] == f2:
                count += 1
                if fruits[j] == f1:
                    last_seen[0] = j
                else:
                    last_seen[1] = j
            elif f1 != -1 and f2 != -1:
                if last_seen[1] < last_seen[0]:
                    count -= last_seen[1] - i
                    i = last_seen[1] + 1
                    last_seen[1] = j
                    f2 = fruits[j]
                else:
                    count -= last_seen[0] - i
                    i = last_seen[0] + 1
                    last_seen[0] = j
                    f1 = fruits[j]
            else:
                if last_seen[0] == -1:
                    count += 1
                    last_seen[0] = j
                    f1 = fruits[j]
                else:
                    count += 1
                    last_seen[1] = j
                    f2 = fruits[j]
            ans = max(ans, count)
        return ans
