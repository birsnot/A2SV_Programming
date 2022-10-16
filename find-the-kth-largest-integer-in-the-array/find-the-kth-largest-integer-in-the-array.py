class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        def qselect(pivot, nums, k):
            greater = []
            less = []
            equal = []

            for num in nums:
                if num > pivot:
                    greater.append(num)
                elif num < pivot:
                    less.append(num)
                else:
                    equal.append(num)

            if k <= len(greater):
                return qselect(pivot=random.choice(greater), nums=greater, k=k)
            elif k <= len(greater) + len(equal):
                return equal[0]
            else:
                new_k = k - len(greater) - len(equal)
                return qselect(pivot=random.choice(less), nums=less, k=new_k)

        lens = [0 for _ in range(101)]
        for num in nums:
            lens[len(num)] += 1

        n = 0
        l = 0
        for i in range(100, 0, -1):
            n += lens[i]
            if n >= k:
                l = i
                break

        new_k = lens[l] - (n - k)

        pivot = ""
        j = 0

        for j in range(len(nums)):
            if len(nums[j]) == l:
                pivot = nums[j]
                break

        greater = []
        less = []
        equal = []

        while j < len(nums):
            if len(nums[j]) == l:
                if nums[j] > pivot:
                    greater.append(nums[j])
                elif nums[j] < pivot:
                    less.append(nums[j])
                else:
                    equal.append(nums[j])
            j += 1

        if new_k <= len(greater):
            return qselect(pivot=random.choice(greater), nums=greater, k=new_k)
        elif new_k <= len(greater) + len(equal):
            return equal[0]
        else:
            new_k = new_k - len(greater) - len(equal)
            return qselect(pivot=random.choice(less), nums=less, k=new_k)
