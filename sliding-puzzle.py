class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        down, up, left, right = (1, 0), (-1, 0), (0, -1), (0, 1)
        drc = (
            ((down, right), (left, down, right), (left, down)),
            ((up, right), (left, up, right), (left, up)))
        check = [[1, 2, 3], [4, 5, 0]]

        dq = deque()
        r = c = 0
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    r = i
                    c = j
                    break
        dq = deque([(r, c, board)])
        visited = set()
        visited.add((tuple(board[0]), tuple(board[1])))
        moves = -1
        while dq:
            moves += 1
            for _ in range(len(dq)):
                r, c, cur_board = dq.popleft()
                if cur_board == check:
                    return moves
                for dr, dc in drc[r][c]:
                    nr = r + dr
                    nc = c + dc
                    new_board = [cur_board[0].copy(), cur_board[1].copy()]
                    new_board[r][c] = new_board[nr][nc]
                    new_board[nr][nc] = 0
                    new_board_tuple = (tuple(new_board[0]), tuple(new_board[1]))
                    if new_board_tuple not in visited:
                        visited.add(new_board_tuple)
                        dq.append((nr, nc, new_board))
        return -1