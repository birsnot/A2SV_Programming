class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        for p, s in zip(position, speed):
            time.append((target-p)/s)
        stack = []
        min_time = -1
        ans = 0
        for i in sorted(range(len(position)), key=lambda i: position[i], reverse=True):
            if time[i] > min_time:
                ans += 1
                min_time = time[i]
        return ans
