class Solution:
    def interpret(self, command: str) -> str:
        i = 0 
        len_str = len(command)
        ans = ''
        while i < len_str:
            if command[i] == 'G':
                ans += 'G'
                i += 1
            elif command[i:i+2] == '()':
                ans += 'o'
                i += 2
            else:
                ans += 'al'
                i += 4
        return ans