class Solution:
    def compress(self, chars: List[str]) -> int:
        cur = 0
        prev = chars[0]
        count = 1
        for ch in chars[1:]:
            if ch == prev:
                count += 1
            else:
                chars[cur] = prev
                cur += 1
                if count > 1:
                    num = str(count)
                    for d in num:
                        chars[cur] = d
                        cur += 1
                count = 1
                prev = ch
        chars[cur] = prev
        cur += 1
        if count > 1:
            num = str(count)
            for d in num:
                chars[cur] = d
                cur += 1
        return cur