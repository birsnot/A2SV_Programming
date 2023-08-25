class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        less = []
        more = [deque([-nums[0]])]
        for n in nums[1:]:
            if more[0][0] == 1 - n:
                cur = heappop(more)
                cur.appendleft(-n)
                if more and more[0][0] == 1 - n:
                    heappush(less, cur)
                    less, more = more, less
                else:
                    heappush(more, cur)
            elif more[0][0] == -n:
                if less and less[0][0] == 1 - n:
                    cur = heappop(less)
                    cur.appendleft(-n)
                    heappush(more, cur)
                else:
                    while less:
                        if len(heappop(less)) < 3:
                            return False
                    heappush(more, deque([-n]))
            else:
                while more:
                    if len(heappop(more)) < 3:
                        return False
                while less:
                    if len(heappop(less)) < 3:
                        return False
                heappush(more, deque([-n]))
        for subs in less:
            if len(subs) < 3:
                return False
        for subs in more:
            if len(subs) < 3:
                return False
        return True