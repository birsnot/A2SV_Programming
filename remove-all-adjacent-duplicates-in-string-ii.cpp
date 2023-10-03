class Solution {
public:
    string removeDuplicates(string s, int k) {
        vector<pair<char, int>> stk;
        for(auto ch: s){
            if (!stk.empty() && ch == stk.back().first){
                if(stk.back().second == k - 1) stk.pop_back();
                else stk.back().second++;
            }
            else stk.push_back({ch, 1});
        }
        string ans;
        for (auto &[ch, fq]: stk){
            for (int i = 0; i < fq; ++i) ans += ch;
        }
        return ans;
    }
};