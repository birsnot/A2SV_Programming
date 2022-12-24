class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        cases = set()
        for n in arr:
            if n in cases:
                return True
            cases.add(n*2)
            cases.add(n/2)
        return False