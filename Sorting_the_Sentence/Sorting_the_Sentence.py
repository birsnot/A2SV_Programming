class Solution:
    def sortSentence(self, s: str) -> str:
        ans = ""
        for n in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            result = re.search(r"\w+(?={})".format(n), s)
            if result == None:
                break
            ans += result.group() + " "
        return ans[:-1]
