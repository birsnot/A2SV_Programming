class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        def qselect(arr, k):
            fq = cnt[choice(arr)]
            less, more = [], []
            for n in arr:
                if cnt[n] < fq:
                    less.append(n)
                else:
                    more.append(n)
            if len(more) < k:
                more.extend(qselect(less, k - len(more)))
                return more
            elif len(more) > k:
                return qselect(more, k)
            return more
        return qselect(list(cnt), k)