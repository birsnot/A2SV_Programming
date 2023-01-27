class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        s1 = deque(word1)
        s2 = deque(word2)
        ans = []
        while s1 and s2:
            if s1[0] > s2[0]:
                ans.append(s1.popleft())
            elif s1[0] < s2[0]:
                ans.append(s2.popleft())
            else:
                temp1 = s1 + s2
                temp2 = s2 + s1
                if temp1 > temp2:
                    ans.append(s1.popleft())
                else:
                    ans.append(s2.popleft())
        if s1:
            ans.extend(s1)
        elif s2:
            ans.extend(s2)
        return "".join(ans)