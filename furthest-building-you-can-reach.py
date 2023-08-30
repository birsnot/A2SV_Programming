class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        gaps = [0]*ladders
        prev = heights[0]
        for i, n in enumerate(heights):
            if n > prev:
                bricks -= heappushpop(gaps, n - prev)
                if bricks < 0:
                    return i - 1
            prev = n
        return len(heights) - 1