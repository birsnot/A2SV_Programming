int trie[490005][52], trie_size;

class WordFilter {
public:
    WordFilter(vector<string>& words) {
        trie_size = 1;
        fill(trie[0], trie[0] + 52, -1);
        for(int i = words.size() - 1; i >= 0; --i) insert(words[i], i);
    }

    void insert(string &word, int i){
        int cur = 0, n = word.size(), idx, suf_cur;
        for(auto ch: word){
            idx = ch - 'a';
            if(trie[cur][idx] == -1){
                fill(trie[trie_size], trie[trie_size] + 52, -1);
                trie[cur][idx] = trie_size++;
            }
            cur = trie[cur][idx];
            suf_cur = cur;
            for(int j = n - 1; j >= 0; --j){
                idx = 26 + word[j] - 'a';
                if(trie[suf_cur][idx] == -1){
                    fill(trie[trie_size] + 26, trie[trie_size] + 52, -1);
                    trie[trie_size][25] = i;
                    trie[suf_cur][idx] = trie_size++;
                }
                suf_cur = trie[suf_cur][idx];
            }
        }
    }
    
    int f(string pref, string suff) {
        int cur = 0, idx, n = suff.size();
        for(auto ch: pref){
            idx = ch - 'a';
            if(trie[cur][idx] == -1) return -1;
            cur = trie[cur][idx];
        }
        for(int j = n - 1; j >= 0; --j){
            idx = 26 + suff[j] - 'a';
            if(trie[cur][idx] == -1) return -1;
            cur = trie[cur][idx];
        }
        return trie[cur][25];
    }
};

/**
 * Your WordFilter object will be instantiated and called as such:
 * WordFilter* obj = new WordFilter(words);
 * int param_1 = obj->f(pref,suff);
 */