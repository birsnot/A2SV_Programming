class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cnts = []
        for n, cnt in sorted(Counter(nums).items()):
            cnts.append((n, n*cnt))
        
        delete = earn = 0
        prev = -1
        for n, cnt in cnts:
            if n == prev + 1:
                new_earn = max(earn, delete + cnt)
                delete = earn
                earn = new_earn
            else:
                delete = earn
                earn += cnt
            prev = n
        return max(earn, delete)