class Solution(object):
    def kClosest(self, points, k):
        def quick_select(points, k):
            pivot = random.choice(points)
            pivot_dis = pivot[0]**2 + pivot[1]**2
            below = []
            equal = []
            above = []
            for [x, y] in points:
                dis = x**2 + y**2
                if dis < pivot_dis:
                    below.append([x, y])
                elif dis == pivot_dis:
                    equal.append([x, y])
                else:
                    above.append([x, y])
            if k < len(below):
                return quick_select(below, k)
            elif k <= len(below) + len(equal):
                return below + equal[:k-len(below)]
            else:
                return below + equal + quick_select(above, k-len(below)-len(equal))
        return quick_select(points, k)
