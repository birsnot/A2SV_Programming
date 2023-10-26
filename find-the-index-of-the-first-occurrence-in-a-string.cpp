class Solution {

public:
    int strStr(string haystack, string needle) {
        int M = needle.size(), N = haystack.size();
        long long m_26 = 1, sub_hash = 0, win_hash = 0, MOD = 1000000007;
        
        for(int i = 0; i < M - 1; ++i){
            sub_hash = sub_hash*26 + needle[i] - 'a';
            win_hash = win_hash*26 + haystack[i] - 'a';
            m_26 *= 26;
            sub_hash %= MOD;
            win_hash %= MOD;
            m_26 %= MOD;
        }
        
        sub_hash = sub_hash*26 + needle[M - 1] - 'a';
        sub_hash %= MOD;

        for(int i = M - 1; i < N; ++i){
            win_hash = win_hash*26 + haystack[i] - 'a';
            win_hash %= MOD;
            if(win_hash == sub_hash){
                bool ok = true;
                for(int p1 = i - M + 1, p2 = 0; p2 < M; ++p1, ++p2){
                    if(haystack[p1] != needle[p2]){
                        ok = false;
                        break;
                    }
                }
                if(ok) return i - M + 1;
            }
            win_hash -= (m_26*(haystack[i - M + 1] - 'a'));
            while(win_hash < 0) win_hash += MOD;
        }
        return -1;
    }
};