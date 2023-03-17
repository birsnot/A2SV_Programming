class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        N = len(num)
        sofar = []
        def helper(i):
            if i >= N:
                return len(sofar) > 2
            for j in range(i+1, N+1):
                n = int(num[i:j])
                if (num[i] != "0" or n == 0) and (len(sofar) < 2 or n == sofar[-1] + sofar[-2]):
                    sofar.append(n)
                    if helper(j):
                        return True
                    sofar.pop()
            return False
        return helper(0)