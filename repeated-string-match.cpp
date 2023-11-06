class Solution {
public:
    int repeatedStringMatch(string a, string b) {
        int N = a.size(), M = b.size();
        vector<int> lps(M);
        int prev_lps = 0, i = 1;
        while(i < M){
            if(b[i] == b[prev_lps]) lps[i++] = ++prev_lps;
            else if(!prev_lps) i++;
            else prev_lps = lps[prev_lps - 1];
        }

        int j = 0; i = 0;
        while(i < N){
            while(j < M && a[i%N] == b[j]){
                i++; j++;
            }
            if(j == M) break;
            if(!j) i++;
            else j = lps[i - 1];
        }
        return (i + N - 1)/N;
    }
};