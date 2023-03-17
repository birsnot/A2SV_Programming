class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        count = defaultdict(int)
        max_ = 0
        max_p = 0
        leads = [0]*len(persons)
        for i, p in enumerate(persons):
            count[p] += 1
            if count[p] >= max_:
                max_ = count[p]
                max_p = p
            leads[i] = max_p
        self.leads = leads
        self.times = times

    def search(self, t):
        l = 0
        r = len(self.times) - 1
        while l <= r:
            mid = (l + r)>>1
            if self.times[mid] > t:
                r = mid - 1
            elif self.times[mid] < t:
                l = mid + 1
            else:
                return mid
        return r

    def q(self, t: int) -> int:
        return self.leads[self.search(t)]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)