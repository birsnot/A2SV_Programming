class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        ios::sync_with_stdio(0);
        cin.tie(0);
        
        int p_count[128] = {};
        for (int i = 0; i < p.length(); ++i){
            p_count[p[i]] += 1;
        }
        int s_count[128] = {};
        int count = 0, l = 0;
        vector <int> ans;
        for(int i = 0; i < s.length(); ++i){
            if (p_count[s[i]] == 0){
                for(int j = 0; j < 128; ++j) s_count[j] = 0;
                l = i + 1;
                count = 0;
            }
            else{
                if(p_count[s[i]] > s_count[s[i]]){
                    ++count;
                    ++s_count[s[i]];
                    if (count == p.length()){
                        ans.push_back(l);
                        --count;
                        --s_count[s[l]];
                        ++l;
                    }
                }
                else{
                    while(s[l] != s[i]){
                        --s_count[s[l]];
                        ++l;
                        --count;
                    }
                    ++l;
                }
            }
        }
        return ans;
    }
};