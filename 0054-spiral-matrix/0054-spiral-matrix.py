class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        ans = matrix[0]
        ans_len = n*m
        top_end = 1
        right_end = n-1
        bottom_end = m-1
        left_end = 0
        while len(ans) != ans_len:
            # move down
            for row in range(top_end, bottom_end+1):
                ans.append(matrix[row][right_end])
            right_end -= 1
                
            #move_left
            for col in range(right_end, left_end-1, -1):
                ans.append(matrix[bottom_end][col])
            bottom_end -= 1
            if len(ans) == ans_len:
                break
            
            #move_up
            for row in range(bottom_end, top_end-1, -1):
                ans.append(matrix[row][left_end])
            left_end += 1
            
            #move_right
            for col in range(left_end, right_end+1):
                ans.append(matrix[top_end][col])
            top_end += 1
        return ans