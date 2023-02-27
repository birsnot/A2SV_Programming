class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int count = 0, l = 0, len = s1.length();
        char ch;
        vector <int> chars1(128);
        for(auto ch: s1){
            chars1[ch] += 1;
        }
        vector <int> chars2(128);
        for(int i = 0;i < s2.length(); ++i){
            ch = s2[i];
            if (chars1[ch] != 0){
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
                chars2 = vector <int>(128);
                count = 0;
                l = i + 1;
            }
        }
        return false;
    }
};