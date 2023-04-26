class Solution {
public:
    void dfs(int v, vector<vector<int>> &graph){
        if (v == end){
            ans.push_back(cur);
            return;
        }
        for(auto u: graph[v]){
                cur.push_back(u);
                dfs(u, graph);
                cur.pop_back();
        }
    }
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        end = graph.size() - 1;
        dfs(0, graph);
        return ans;
    }
private:
    int end;
    vector<vector<int>> ans;
    vector<int> cur = {0};
};