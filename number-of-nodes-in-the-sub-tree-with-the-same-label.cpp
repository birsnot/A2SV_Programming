class Solution {
public:
    vector<int> countSubTrees(int n, vector<vector<int>>& edges, string labels) {
        vector<int> adj[n];
        for(auto &e: edges){
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        vector<int> visited(n);
        vector<int> count(26);
        vector<int> ans(n);

        function<void(int)> dfs = [&](int v){
            ++visited[v];
            int ch = labels[v] - 97;
            int before = count[ch]++;
            for(auto u: adj[v]){
                if(!visited[u]) dfs(u);
            }
            ans[v] = count[ch] - before;
        };
        dfs(0);
        return ans;
    }
};