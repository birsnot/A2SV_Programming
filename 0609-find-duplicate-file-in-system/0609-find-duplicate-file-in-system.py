class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        files = {}
        for path in paths:
            i = 0
            while path[i] != ' ':
                i += 1
            d_idx = i  #ending index for directory name
            f_left = i+1 #starting index for file name
            f_right = 0 #ending index for file name
            while i < len(path):
                if path[i] == '(':
                    f_right = i
                    c_left = i + 1 # starting index for the content
                    while path[i] != ')':
                        i += 1
                    c_right = i #ending index for the content
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