class Solution {
public:
    string shiftingLetters(string s, vector<vector<int>>& shifts) {
        int N = s.length() + 1;
        vector <int> accu(N);
        for(auto &shift: shifts){
            if(shift[2]){
                accu[shift[0]] += 1;
                accu[shift[1] + 1] -= 1;
            }
            else{
                accu[shift[0]] -= 1;
                accu[shift[1] + 1] += 1;
            }
        }
        for(int i = 1; i < N; ++i){
            accu[i] += accu[i - 1];
        }
        string chars = "abcdefghijklmnopqrstuvwxyz";
        for(int i = 0; i < s.length(); ++i){
            int idx = (int)s[i] - 97 + accu[i];
            idx = (idx%26 + 26)%26;
            s[i] = chars[idx];
        }
        return s;
    }
};