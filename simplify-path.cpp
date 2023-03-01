class Solution {
public:
    string simplifyPath(string path) {
        vector <string> ans;
        vector <string> paths = split(path);
        for (auto p: paths){
            if (p == ".."){
                if(!ans.empty()) ans.pop_back();
            }
            else if(p != "." and p != ""){
                ans.push_back(p);
            }
        }
        for (auto p: paths){
            cout << p << "\n";
        }
        string ret;
        for (auto p: ans){
            ret += "/" + p;
        }
        if(ret != "") return ret;
        return "/";
    }
    vector <string> split(const string& path){
        vector <string> paths;
        string p;
        for(auto ch: path){
            if (ch != '/'){
                p += ch;
            }
            else if (p != ""){
                paths.push_back(p);
                p = "";
            }
        }
        if (p != "") paths.push_back(p);
        return paths;
    }
};