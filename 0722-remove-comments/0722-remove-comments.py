class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = [""]
        i = 0
        source_len = len(source)
        cur = 0
        while i < source_len:
            j = 0
            while j < len(source[i]):
                if j < len(source[i])-1 and source[i][j:j+2] == "//":
                    break
                elif j < len(source[i])-1 and source[i][j:j+2] == "/*":
                    j += 2
                    found = False
                    while True:
                        while j < len(source[i]):
                            if j < len(source[i])-1 and source[i][j:j+2] == "*/":
                                j += 2
                                found = True
                                break
                            else:
                                j += 1
                        if found:
                            break
                        j = 0
                        i += 1
                else:
                    ans[cur] += source[i][j]
                    j += 1
            if ans[-1] != "":
                ans.append("")
                cur += 1
            i += 1
        return ans[:-1]