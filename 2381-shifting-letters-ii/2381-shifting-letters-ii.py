class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        chars = "abcdefghijklmnopqrstuvwxyz"
        N = len(s) + 1
        accu = [0]*N
        for st, end, move in shifts:
            if move:
                accu[st] += 1
                accu[end + 1] -= 1
            else:
                accu[st] -= 1
                accu[end + 1] += 1
        for i in range(1, N):
            accu[i] += accu[i - 1]
        ans = []
        for i, ch in enumerate(s):
            idx = (ord(ch) - 97 + accu[i])%26
            ans.append(chars[idx])
        return "".join(ans)