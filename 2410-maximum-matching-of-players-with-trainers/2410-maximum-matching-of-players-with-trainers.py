class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        P = len(players)
        T = len(trainers)
        p_idx = 0
        t_idx = 0
        ans = 0
        while p_idx < P and t_idx < T:
            if trainers[t_idx] >= players[p_idx]:
                ans += 1
                t_idx += 1
                p_idx += 1
            else:
                p_idx += 1
        return ans