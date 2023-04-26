class Solution {
public:
    bool possibleBipartition(int n, vector<vector<int>>& dislikes) {
        ios::sync_with_stdio(0);
        cin.tie(0);

        vector<int> adj[n + 1];
        vector<int> visited(n + 1);

        for(auto e: dislikes){
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        function<bool(int, int)> dfs = [&](int v, int prev){
            int cur = prev^3;
            visited[v] = cur;
            for (auto u: adj[v]){
                if (!visited[u]){
                    if (!dfs(u, cur)) return false;
                }
                else if (visited[u] == cur){
                    return false;
                }
            }
            return true;
        };
        for (int v = 1; v <= n; ++v){
            if(!visited[v] and !dfs(v, 1))
                return false;
        }
        return true;
    }
};