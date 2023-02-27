class Solution {
public:
    int characterReplacement(string s, int k) {
        int max_ = 0, k_ = k, l = 0;
        unordered_map<char, int> chars;
        for(auto ch: s){
            chars[ch] += 1;
            if (chars[ch] > max_){
                max_ += 1;
            }
            else{
                k_ -= 1;
            }
            if (k_ < 0){
                chars[s[l]] -= 1;
                k_ += 1;
                l += 1;
            }
        }
        return max_ - k_ + k;
    }
};