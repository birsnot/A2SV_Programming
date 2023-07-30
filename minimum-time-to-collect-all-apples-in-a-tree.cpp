class Solution {
public:
    int minTime(int n, vector<vector<int>>& edges, vector<bool>& hasApple) {
        vector<int> adj[n];
        for(auto e: edges){
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }

        vector<bool> visited(n);
        
        function<bool(int)> dfs = [&](int v){
            bool gotApple = hasApple[v];
            for(auto ch: adj[v]){
                if(visited[ch]) continue;
                visited[ch] = true;
                gotApple = dfs(ch) || gotApple;
            }
            hasApple[v] = gotApple;
            return gotApple;
        };

        visited[0] = true;
        dfs(0);
        if(!hasApple[0]) return 0;
        return 2*(accumulate(hasApple.begin(), hasApple.end(), 0) - 1);
    }
};