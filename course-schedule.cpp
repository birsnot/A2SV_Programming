class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> visited(numCourses);
        vector<int> adj[numCourses];
        for(const auto& v: prerequisites) adj[v[1]].push_back(v[0]);
        function<bool(int)> dfs = [&](int v){
            visited[v] = 1;
            for(auto ch: adj[v]){
                if(visited[ch] == 0){
                    if(!dfs(ch)) return false;
                }
                else if(visited[ch] == 1) return false;
            }
            visited[v] = 2;
            return true;
        };
        for(int i = 0; i < numCourses; ++i){
            if(visited[i] == 0)
                if(!dfs(i)) return false;
        }
        return true;
    }
};