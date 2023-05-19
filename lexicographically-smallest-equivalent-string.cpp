class Solution {
public:
    Solution(): rep(26) {
        iota(rep.begin(), rep.end(), 0);
    }
    vector<int> rep;
    int find(int ch){
        if(ch == rep[ch]) return ch;
        rep[ch] = find(rep[ch]);
        return rep[ch];
    }
    void merge(int x, int y){
        x = find(x);
        y = find(y);
        if(x == y) return;
        if(x > y) swap(x, y);
        rep[y] = x;
    }
    string smallestEquivalentString(string s1, string s2, string baseStr) {
        for(int i = 0; i < s1.size(); ++i) merge(s1[i] - 'a', s2[i] - 'a');
        string ans;
        for(int i = 0; i < baseStr.size(); ++i) ans += 'a' + find(baseStr[i] - 'a');
        return ans;
    }
};