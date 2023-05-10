class Solution {
public:
    vector<string> findAllRecipes(vector<string>& recipes, vector<vector<string>>& ing, vector<string>& supplies) {
        unordered_map<string, int> idx;
        vector<int> dp(recipes.size());
        unordered_set<string> sup(supplies.begin(), supplies.end());
        for(int i = 0; i < recipes.size(); ++i){
            idx[recipes[i]] = i;
        }
        vector<string> ans;
        for(int i = 0; i < recipes.size(); ++i){
            if(dp[i]){
                if(dp[i] == 1) ans.push_back(recipes[i]);
            }
            else{
                if(dfs(recipes[i], ing, idx, dp, sup)) ans.push_back(recipes[i]);
            }
        }
        return ans;
    }
private:
        bool dfs(string v, vector<vector<string>>& ing, unordered_map<string, int>& idx, vector<int>& dp, unordered_set<string>& sup){
            int i = idx[v];
            if(dp[i]) return dp[i] == 1;
            dp[i] = 2;
            for(string ch: ing[i]){
                if(sup.count(ch)) continue;
                if(!idx.count(ch)) return false;
                if(!dfs(ch, ing, idx, dp, sup)){
                    return false;
                }
            }
            dp[i] = 1;
            return true;
        };

};