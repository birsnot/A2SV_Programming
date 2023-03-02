class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos = sorted(range(len(speed)), key=lambda i: position[i], reverse=True)
        ans = 0
        prev_t = 0
        for i in pos:
            p, s = position[i], speed[i]
            t = (target - p)/s
            if t > prev_t:
                ans += 1
                prev_t = t
        return ans