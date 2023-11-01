class Solution {
public:
    int maximumPopulation(vector<vector<int>>& logs) {
        int line[102];
        memset(line, 0, sizeof line);
        for(auto log: logs){
            line[log[0] - 1950]++;
            line[log[1] - 1950]--;
        }
        int ans = 1950, max_ = line[0];
        for(int i = 1; i < 102; ++i){
            line[i] += line[i - 1];
            if(line[i] > max_){
                ans = i + 1950;
                max_ = line[i];
            }
        }
        return ans;
    }
};