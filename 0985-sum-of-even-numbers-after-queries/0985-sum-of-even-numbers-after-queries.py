class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        last_sum = 0
        for n in nums:
            if n%2 == 0:
                last_sum += n
        
        ans = []
        for val, idx in queries:
            n_old = nums[idx]
            nums[idx] = n = n_old + val
            if n%2 == 0:
                if val%2 == 0:
                    last_sum += val
                else:
                    last_sum += n
            elif n_old%2 == 0:
                last_sum -= n_old
            ans.append(last_sum)
        
        return ans