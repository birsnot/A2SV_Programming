class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickselect(arr, k):
            p = choice(arr)
            less, more, equal = [], [], 0
            for n in arr:
                if n < p:
                    less.append(n)
                elif n > p:
                    more.append(n)
                else:
                    equal += 1
            if len(more) >= k:
                return quickselect(more, k)
            elif len(more) + equal >= k:
                return p
            else:
                return quickselect(less, k - len(more) - equal)
        return quickselect(nums, k)