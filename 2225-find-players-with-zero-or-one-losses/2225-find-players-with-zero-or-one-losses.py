class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = {}
        for win, lose in matches:
            if win not in players:
                players[win] = 0
            if lose in players:
                players[lose] += 1
            else:
                players[lose] = 1
        winners = []
        lost_1s = []
        for p in players:
            if players[p] == 0:
                winners.append(p)
            elif players[p] == 1:
                lost_1s.append(p)
        return [sorted(winners), sorted(lost_1s)]