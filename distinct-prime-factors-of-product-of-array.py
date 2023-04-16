class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        found = [0]*11
        nums = set(nums)
        ans = set()
        for n in nums:
            i = 0
            while i < 11:
                p = primes[i]
                if n%p == 0:
                    found[i] = 1
                    while n%p == 0:
                        n //= p
                elif n == 1:
                    break
                i += 1
            if n > 1:
                ans.add(n)
        return len(ans) + sum(found)