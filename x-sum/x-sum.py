T = int(input())
for _ in range(T):
    n, m = list(map(int, input().split()))
    board = []
    for __ in range(n):
        row = list(map(int, input().split()))
        board.append(row)
    main_diag = [0]*(n + m - 1)
    offset = n - 1
    anti_diag = [0]*(n + m - 1)
    for r, row in enumerate(board):
        for c, val in enumerate(row):
            main_diag[c - r + offset] += val
            anti_diag[c + r] += val

    ans = 0
    for r, row in enumerate(board):
        for c, val in enumerate(row):
            sum_ = main_diag[c - r + offset] + anti_diag[c + r] - val
            ans = max(ans, sum_)
    print(ans)
