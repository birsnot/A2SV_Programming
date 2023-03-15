class Solution:
    def balancedString(self, s: str) -> int:
        count = [0]*4
        qwer = "QWER"
        for ch in s:
            count[qwer.index(ch)] += 1
        target = len(s)//4
        replace = [0]*4
        for i, n in enumerate(count):
            if n > target:
                replace[i] = n - target
        window = [0]*4
        if replace == window:
            return 0
        def check():
            for i in range(4):
                if window[i] < replace[i]:
                    return False
            return True
        l = 0
        ans = len(s)
        for i, ch in enumerate(s):
            window[qwer.index(ch)] += 1
            while check():
                window[qwer.index(s[l])] -= 1
                ans = min(ans, i - l)
                l += 1
        return ans + 1