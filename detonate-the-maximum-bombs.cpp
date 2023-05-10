class Solution {
public:
    int maximumDetonation(vector<vector<int>>& bombs) {
        const int N = bombs.size();
        vector<int> adj[N];
        long long x, y, rr1, rr2, dx, dy, rr;
        for(int i = 0; i < N; ++i){
            x = bombs[i][0], y = bombs[i][1], rr1 = 1ll*bombs[i][2]*bombs[i][2];
            for(int j = i + 1; j < N; ++j){
                dx = x - bombs[j][0], dy = y - bombs[j][1];
                rr = dx*dx + dy*dy;
                rr2 = 1ll*bombs[j][2]*bombs[j][2];
                if(rr <= rr1) adj[i].push_back(j);
                if(rr <= rr2) adj[j].push_back(i);
            }
        }
        int ans = 0;
        unordered_set<int> visited;
        for(int i = 0; i < N; ++i){
            if(!visited.count(i)){
                visited = {};
                visited.insert(i);
                ans = max(ans, dfs(i, adj, visited));
            }
        }
        return ans;
    }
private:
        int dfs(int v, vector<int>* adj, unordered_set<int>& visited){
            int ret = 1;
            for(auto ch: adj[v]){
                if(!visited.count(ch)){
                    visited.insert(ch);
                    ret += dfs(ch, adj, visited);
                }
            }
            return ret;
        }
};