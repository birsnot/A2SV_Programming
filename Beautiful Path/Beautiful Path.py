m, n = list(map(int, input().split()))
road = []
for _ in range(m):
    row = input()
    road.append(row)
road_ = []
for col in zip(*road):
    road_.append(col)
t_col = s_col = t_row = s_row = 0
for r, row in enumerate(road):
    for c, val in enumerate(row):
        if val == "S":
            s_row = r
            s_col = c
        if val == "T":
            t_row = r
            t_col = c
found = False
for r, row in enumerate(road):
    if "*" not in row[t_col:s_col + 1] and "*" not in row[s_col:t_col + 1]:
        if "*" not in road_[t_col][r:t_row] and "*" not in road_[t_col][t_row:r]:
            if "*" not in road_[s_col][r:s_row] and "*" not in road_[s_col][s_row:r]:
                found = True
if not found:
    s_col, s_row = s_row, s_col
    t_col, t_row = t_row, t_col
    for r, row in enumerate(road_):
        if "*" not in row[t_col:s_col + 1] and "*" not in row[s_col:t_col + 1]:
            if "*" not in road[t_col][r:t_row] and "*" not in road[t_col][t_row:r]:
                if "*" not in road[s_col][r:s_row] and "*" not in road[s_col][s_row:r]:
                    found = True
if found:
    print("YES")
else:
    print("NO")
