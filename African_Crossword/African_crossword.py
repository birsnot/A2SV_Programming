from collections import Counter


m, n = list(map(int, input().split()))
crossword = []
for _ in range(m):
    row = input()
    crossword.append(row)
rows = [{}]*m
cols = [{}]*n
for r, row in enumerate(crossword):
    rows[r] = Counter(row)
for c, col in enumerate(zip(*crossword)):
    cols[c] = Counter(col)

ans = []
for r, row in enumerate(crossword):
    for c, val in enumerate(row):
        if rows[r][val] == 1 and cols[c][val] == 1:
            ans.append(val)
print("".join(ans))
