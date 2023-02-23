class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        ios::sync_with_stdio(0);
        cin.tie(0);
        
        unordered_map<char, int> pChars;
        for(int i = 0; i < p.length(); ++i){
            pChars[p[i]] += 1;
        }
        unordered_map<char, int> check;
        for(auto ch: pChars){
            check[ch.first] = 0;
        }
        vector <int> ans;
        int count = 0;
        int l = 0;
        for(int i = 0; i < s.length(); ++i){
            if (check.find(s[i]) != check.end()){
                if(check[s[i]] < pChars[s[i]]){
                    ++check[s[i]];
                    ++count;
                    if (count == p.length()){
                        ans.push_back(l);
                        --check[s[l]];
                        --count;
                        ++l;
                    }
                }
                else{
                    while(s[l] != s[i]){
                        --check[s[l]];
                        --count;
                        ++l;
                    }
                    ++l;
                }
            }
            else{
                for(auto ch: pChars){
                    check[ch.first] = 0;
                }
                count = 0;
                l = i + 1;
            }
        }
        return ans;
    }
};