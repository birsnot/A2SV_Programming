class Solution {
public:
    string longestPrefix(string s) {
        int prev_lps = 0, i = 1, M = s.size();
        vector<int> lps(M);
        while(i < M){
            if(s[i] == s[prev_lps]) lps[i++] = ++prev_lps;
            else{
                if(!prev_lps) i++;
                else prev_lps = lps[prev_lps - 1];
            }
        }
        return s.substr(0, lps[M - 1]);
    }
};