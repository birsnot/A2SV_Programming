class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        N = len(intervals)
        starts = [0]*N
        for i, (st, _) in enumerate(intervals):
            starts[i] = (st, i)
        starts.sort()
        ans = [0]*N
        def search(end):
            l = 0
            r = N - 1
            while l <= r:
                mid = (l + r)>>1
                if starts[mid][0] < end:
                    l = mid + 1
                else:
                    r = mid - 1
            if l >= N: return -1
            return starts[l][1]

        for i, (_, end) in enumerate(intervals):
            ans[i] = search(end)
        return ans