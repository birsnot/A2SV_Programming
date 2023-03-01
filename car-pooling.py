class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        kms = [0]*1001
        for p, f, t in trips:
            kms[f] += p
            kms[t] -= p
        ps = 0
        for km in kms:
            ps += km
            if ps > capacity:
                return False
        return True