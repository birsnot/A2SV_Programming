class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def get_rc(x):
            x -= 1
            r = x//n
            if r&1:
                c = n - 1 - x%n
            else:
                c = x%n
            return (n - 1 - r, c)

        dq = deque([1])
        visited = set()
        nn = n*n
        moves = 0
        while dq:
            moves += 1
            L = len(dq)
            for _ in range(L):
                cur = dq.popleft()
                if cur + 6 >= nn:
                    return moves
                for i in range(1, 7):
                    r, c = get_rc(cur + i)
                    if board[r][c] != -1:
                        next = board[r][c]
                        if next >= nn:
                            return moves
                    else:
                        next = cur + i
                    if next not in visited:
                        visited.add(next)
                        dq.append(next)
        return -1