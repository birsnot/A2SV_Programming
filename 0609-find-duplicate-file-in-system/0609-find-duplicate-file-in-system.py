class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        files = {}
        for path in paths:
            i = 0
            while path[i] != ' ':
                i += 1
            d_idx = i
            f_left = i+1
            f_right = 0
            while i < len(path):
                if path[i] == '(':
                    f_right = i
                    c_left = i + 1
                    while path[i] != ')':
                        i += 1
                    c_right = i
                    i += 2
                    content = path[c_left:c_right]
                    dir_ = path[:d_idx]
                    file_name = path[f_left:f_right]
                    if content in files:
                        files[content].append([dir_, file_name])
                    else:
                        files[content] = [[dir_, file_name]]
                    f_left = i
                else:
                    i += 1
        print(files)
        ans = []
        for key in files:
            if len(files[key]) > 1:
                dupl = []
                for file in files[key]:
                    dupl.append("/".join(file))
                ans.append(dupl)
        return ans