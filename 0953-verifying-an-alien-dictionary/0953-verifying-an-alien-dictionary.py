class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        letter_idx = {}
        for idx,letter in enumerate(order):
            letter_idx[letter] = idx
            
        words_len = len(words)-1 
        i = 0
        while i < words_len:
            j = 0
            word1 = words[i]
            word2 = words[i+1]
            word1_len = len(word1)
            word2_len = len(word2)
            while j < word1_len and j < word2_len:
                if letter_idx[word1[j]] > letter_idx[word2[j]]:
                    return False
                if letter_idx[word1[j]] < letter_idx[word2[j]]:
                    break
                j += 1
            if j >= word2_len and j < word1_len:
                return False
            i += 1
        return True