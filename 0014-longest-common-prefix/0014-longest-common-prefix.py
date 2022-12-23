class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        cmn_idx = len(ans) #last common index
        for str in strs[1:]:
            check = min(len(str), cmn_idx)
            i = 0
            while i < check:
                if ans[i] != str[i]:
                    break
                i += 1
            cmn_idx = i
        return ans[:cmn_idx]