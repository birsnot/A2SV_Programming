class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int count = 0, l = 0, len = s1.length();
        char ch;
        unordered_map<char, int> chars1;
        for(auto ch: s1){
            chars1[ch] += 1;
        }
        unordered_map<char, int> chars2;
        for(int i = 0;i < s2.length(); ++i){
            ch = s2[i];
            if (chars1.find(ch) != chars1.end()){
                if(chars2[ch] < chars1[ch]){
                    ++count;
                    ++chars2[ch];
                    if (count == len) return true;
                }
                else{
                    while(s2[l] != ch){
                        --chars2[s2[l]];
                        --count;
                        ++l;
                    }
                    ++l;
                }
            }
            else{
                chars2.clear();
                count = 0;
                l = i + 1;
            }
        }
        return false;
    }
};