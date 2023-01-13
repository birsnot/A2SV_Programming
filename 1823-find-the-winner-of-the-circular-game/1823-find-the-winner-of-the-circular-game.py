class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        survivor = 0
        for persons in range(2, n + 1):
            survivor = (survivor + k)%persons
        return survivor + 1