T = int(input())
for _ in range(T):
    _ = input()
    board = []
    for r in range(8):
        row = input()
        board.append(row)
    ans_r = 0
    ans_c = 0
    done = False
    for r in range(1, 7):
        for c in range(1, 7):
            if board[r][c] == "#":
                if '.' not in [board[r+1][c-1], board[r+1][c+1], board[r-1][c+1], board[r-1][c-1]]:
                    ans_c = c + 1
                    ans_r = r + 1
                    done = True
                    break
        if done:
            break
    print(ans_r, ans_c)
