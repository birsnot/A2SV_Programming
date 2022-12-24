class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        near_idx = -1
        min_d = float('inf')
        
        for i, point in enumerate(points):
            xi, yi = point
            dx = abs(x-xi)
            dy = abs(y-yi)
            
            if dy == 0:
                if dx < min_d:
                    min_d = dx
                    near_idx = i
            elif dx == 0:
                if dy < min_d:
                    min_d = dy
                    near_idx = i
        return near_idx