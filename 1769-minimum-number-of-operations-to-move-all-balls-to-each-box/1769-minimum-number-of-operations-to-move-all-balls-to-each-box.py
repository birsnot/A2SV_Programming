class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        opr = 0
        change = 0
        for i, ball in enumerate(boxes,1):
            if ball == "1":
                change += 1
                opr += i
        ans = []
        for ball in boxes:
            opr -= change
            ans.append(opr)
            if ball == "1":
                change -= 2
        return ans