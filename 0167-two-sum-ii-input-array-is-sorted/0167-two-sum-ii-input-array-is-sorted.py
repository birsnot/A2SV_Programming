import bisect
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            sum = numbers[l] + numbers[r]

            if sum == target:
                return [l + 1, r + 1]
            elif sum > target:
                r = bisect.bisect_right(numbers, target - numbers[l], l, r - 1)
            else:
                l = bisect.bisect_left(numbers, target - numbers[r], l + 1, r)