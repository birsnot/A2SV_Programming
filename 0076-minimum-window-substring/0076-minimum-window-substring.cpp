class Solution {
public:
    string minWindow(string s, string t) {
        vector <int> t_chars(128);
        int l = 0, count = t.length();
        vector <int> ans(2, s.length());
        for(auto ch: t){
            ++t_chars[ch];
        }
        for (int i = 0; i < s.length(); ++i){
            if (t_chars[s[i]] > 0){
                --count;
            }
            --t_chars[s[i]];
            if(count == 0){
                while(1){
                    if (t_chars[s[l]] == 0){
                        break;
                    }
                    ++t_chars[s[l]];
                    ++l;
                }
                if (ans[0] > i - l){
                    ans[0] = i - l;
                    ans[1] = l;
                }
                ++t_chars[s[l]];
                ++count;
                ++l;
            }
        }
        return s.substr(ans[1], ans[0] + 1);
    }
};