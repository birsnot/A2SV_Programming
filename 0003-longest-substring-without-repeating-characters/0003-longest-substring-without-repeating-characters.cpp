class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        ios::sync_with_stdio(0);
        cin.tie(0);
        
        unordered_map < char, int> uniques;
        int start = -1, res = 0, len = s.length();
        for (int i = 0; i < len; ++i){
            if (uniques.find(s[i]) != uniques.end() && uniques[s[i]] > start){
                start = uniques[s[i]];
            }
            uniques[s[i]] = i;
            if (res < i - start){
                res = i - start;
            }
        }
        return res;
    }
};