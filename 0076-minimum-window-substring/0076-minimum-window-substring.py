class Solution:
    def min_idx(self, s_chars):
        min_i = 100000
        for fq in s_chars.values():
            if fq and fq[0] < min_i:
                min_i = fq[0]
        return min_i
    
    def minWindow(self, s: str, t: str) -> str:
        t_chars = Counter(t)
        s_chars = {}
        t_len = len(t)
        count = 0
        min_i = len(s)
        ans = (len(s), 0, 0)
        for i, ch in enumerate(s):
            if ch in t_chars:
                if ch not in s_chars:
                    s_chars[ch] = deque([i])
                    count += 1
                    min_i = min(min_i, i)
                    if count == t_len:
                        if i - min_i < ans[0]:
                            ans = (i - min_i, min_i, i + 1)
                        count -= 1
                        s_chars[s[min_i]].popleft()
                        min_i = self.min_idx(s_chars)
                elif len(s_chars[ch]) < t_chars[ch]:
                    s_chars[ch].append(i)
                    count += 1
                    if count == t_len:
                        if i - min_i < ans[0]:
                            ans = (i - min_i, min_i, i + 1)
                        count -= 1
                        s_chars[s[min_i]].popleft()
                        min_i = self.min_idx(s_chars)
                else:
                    j = s_chars[ch].popleft()
                    s_chars[ch].append(i)
                    if j == min_i:
                        min_i = self.min_idx(s_chars)
        return s[ans[1]:ans[2]]