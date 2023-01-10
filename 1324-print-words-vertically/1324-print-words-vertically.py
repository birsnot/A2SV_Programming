class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        ans = []
        columns = max(len(word) for word in words)
        for col in range(columns):
            spaces = 0
            new_word = []
            for word in words:
                if col < len(word):
                    new_word.extend([" "]*spaces)
                    new_word.append(word[col])
                    spaces = 0
                else:
                    spaces += 1
            ans.append("".join(new_word))
        
        return ans