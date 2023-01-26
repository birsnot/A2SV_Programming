class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        chars = {}
        for i, ch in enumerate(s, 1):
            if ch not in chars:
                chars[ch] = [i, i]
            else:
                chars[ch][1] = i
        ans = []
        part_start = 0
        prev_end = chars[next(iter(chars))][1]
        for start_idx, end_idx in chars.values():
            if start_idx <= prev_end:
                prev_end = max(prev_end, end_idx)
            else:
                new_part = prev_end - part_start
                ans.append(new_part)
                part_start += new_part
                prev_end = end_idx
        ans.append(prev_end - part_start)
        return ans