class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        ones = set()
        for r,row in enumerate(img1):
            for c,col in enumerate(row):
                if col:ones.add((r,c))
        n = len(img1)
        ans = 0
        for i in range(1-n,n):
            for j in range(1-n,n):
                count = 0
                for one in ones:
                    r, c = one[0]+i, one[1]+j
                    if r < n and c < n and r > -1 and c > -1:
                        count += img2[r][c]
                if ans < count:
                    ans = count
        return ans