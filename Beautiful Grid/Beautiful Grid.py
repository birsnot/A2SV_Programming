from collections import Counter


T = int(input())
for _ in range(T):
    n = int(input())
    grid = []
    for r in range(n):
        row = input()
        grid.append(row)
    ans = 0
    len_ = n - 1
    for diag in range(n//2):
        loops = len_ - 2*diag
        for i in range(loops):
            r = diag
            c = diag + i
            freq = Counter([grid[r][c], grid[c][len_-r], grid[len_-r][len_-c],grid[len_-c][r]])
            temp = min(freq.values())
            if temp < 4:
                ans += temp
    print(ans)
