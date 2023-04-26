class Solution {
public:
    int findCircleNum(vector<vector<int>>& adjM) {
        vector<int> visited(adjM.size());
        function<void(int)> dfs = [&](int x){
            visited[x] = 1;
            for (int i = 0; i < adjM.size(); ++i){
                if (!visited[i] && adjM[x][i]){
                    dfs(i);
                }
            }
        };
        int count = 0;
        for (int i = 0; i < adjM.size(); ++i){
            if (!visited[i]){
                ++count;
                dfs(i);
            }
        }
        return count;
    }
};