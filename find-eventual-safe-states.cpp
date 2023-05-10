class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        ios::sync_with_stdio(0);
        cin.tie(0);
        vector<int> visited(graph.size());
        vector<int> ans;
        for(int i = 0; i < graph.size(); ++i){
            if(!visited[i]) dfs(i, graph, visited);
            if(visited[i] == 2) ans.push_back(i);
        }
        return ans;
    }
private:
        bool dfs(int v, vector<vector<int>> &graph, vector<int> &visited){
            visited[v] = 1;
            for(auto ch: graph[v]){
                if(!visited[ch]){
                    if(!dfs(ch, graph, visited)){
                        return false;
                    }
                }
                else if(visited[ch] == 1) return false;
            }
            visited[v] = 2;
            return true;
        };
};