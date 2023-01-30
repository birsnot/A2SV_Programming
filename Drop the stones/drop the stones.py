T = int(input())
for _ in range(T):
    R, C = map(int, input().split())
    grid_ = []
    for __ in range(R):
        grid_.append(input())
    grid = []
    for col in zip(*grid_):
        grid.append(list(col))
    for i, row in enumerate(grid):
        count = 0
        i = 0
        while i < R:
            if row[i] == "*":
                count += 1
                row[i] = "."
            elif row[i] == "o":
                j = i-count
                while j < i:
                    row[j] = "*"
                    j += 1
                count = 0
            i += 1
        j = R-count
        while j < R:
            row[j] = "*"
            j += 1
    for row in zip(*grid):
        print("".join(row))
