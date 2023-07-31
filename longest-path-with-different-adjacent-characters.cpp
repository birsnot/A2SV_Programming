class Solution {
public:
    int longestPath(vector<int>& parent, string s) {
        int N = s.size(), ans = 1;
        vector<int> children[N];
        for(int i = 1; i < N; ++i){
            children[parent[i]].push_back(i);
        }
        
        function<int(int)> dfs = [&](int v){
            int ret = 1;
            vector<int> branches;
            for(auto child: children[v]){
                if(s[child] != s[v]){
                    branches.push_back(dfs(child));
                    continue;
                }
                dfs(child);
            }
            if(!branches.empty()){
                vector<int>::iterator max_ = max_element(branches.begin(), branches.end());
                ret += *max_;
                *max_ = 0;
                max_ = max_element(branches.begin(), branches.end());
                ans = max(ans, ret + *max_);
            }
            return ret;
        };

        dfs(0);
        return ans;
    }
};