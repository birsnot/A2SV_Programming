class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cnt = Counter(s)
        ms = []
        dst = set()
        for ch in s:
            cnt[ch] -= 1
            if ch not in dst:
                while ms and ms[-1] > ch and cnt[ms[-1]]:
                    ch2 = ms.pop()
                    dst.remove(ch2)
                ms.append(ch)
                dst.add(ch)

        return "".join(ms[:])