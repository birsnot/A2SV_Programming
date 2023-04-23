class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        cnt = Counter(deck)
        g = 0
        for fq in cnt.values():
            g = gcd(fq, g)
            if g == 1:
                return False
        return True