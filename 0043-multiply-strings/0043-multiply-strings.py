class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        n1 = list(map(int, num1[::-1]))
        n2 = list(map(int, num2[::-1]))
        ans = [0]*(len(n1) + len(n2))
        shift = 0
        for n in n1:
            for i, m in enumerate(n2, shift):
                product = n*m
                ans[i+1] += product//10
                ans[i] += product%10
            shift += 1
            
        for i,n in enumerate(ans):
            if n > 9:
                ans[i] = n%10
                ans[i+1] += n//10
        
        while ans[-1] == 0:
            ans.pop()
            
        return "".join(map(str, ans[::-1]))