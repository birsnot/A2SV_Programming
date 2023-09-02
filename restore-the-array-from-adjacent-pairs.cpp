class Solution {
public:
    vector<int> restoreArray(vector<vector<int>>& adjacentPairs) {
        vector<int> ans;
        unordered_map<int, vector<int>> adj;
        for(auto v: adjacentPairs){
            adj[v[0]].push_back(v[1]);
            adj[v[1]].push_back(v[0]);
        }
        unordered_set<int> visited;
        function<void(int)> dfs = [&](int v){
            visited.insert(v);
            for(auto ch: adj[v]){
                
                if(visited.count(ch) == 0){
                    dfs(ch);
                }
            }
            ans.push_back(v);
        };
        for(auto& [v, ch]: adj){
            if(ch.size() == 1){
                dfs(v);
                break;
            }
        }
        return ans;
    }
};