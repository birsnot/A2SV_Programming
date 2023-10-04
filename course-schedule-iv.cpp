int dis[100][100];
class Solution {
public:
    vector<bool> checkIfPrerequisite(int numCourses, vector<vector<int>>& prerequisites, vector<vector<int>>& queries) {
        for(int i = 0; i < numCourses; ++i){
            fill(dis[i], dis[i] + numCourses, 1e5);
        }

        for(auto &edge: prerequisites){
            dis[edge[0]][edge[1]] = 1;
        }

        for(int i = 0; i < numCourses; ++i){
            for(int j = 0; j < numCourses; ++j){
                for(int k = 0; k < numCourses; ++k){
                    dis[j][k] = min(dis[j][k], dis[j][i] + dis[i][k]);
                }
            }
        }
        vector<bool> ans;
        for(auto &q: queries){
            ans.push_back(dis[q[0]][q[1]] < 100000);
        }
        return ans;
    }
};