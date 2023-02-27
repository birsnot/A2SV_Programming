class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        sign = ""
        ans = count = 1
        for i, n in enumerate(arr[1:]):
            if sign == "<":
                if n < arr[i]:
                    count += 1
                    sign = ">"
                else:
                    ans = max(ans, count)
                    if n > arr[i]:
                        count = 2
                    else:
                        count = 1
                        sign = ""
            elif sign == ">":
                if n > arr[i]:
                    count += 1
                    sign = "<"
                else:
                    ans = max(ans, count)
                    if n < arr[i]:
                        count = 2
                    else:
                        count = 1
                        sign = ""
            else:
                count = 2
                if n > arr[i]:
                    sign = "<"
                elif n < arr[i]:
                    sign = ">"
                else:
                    count = 1
                    sign = ""
        return max(ans, count)