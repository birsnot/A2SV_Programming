class Solution {
public:
    vector<int> rep;
    vector<vector<char>> str;
    int find(int x){
        while (x != rep[x]){
            x = rep[x] = rep[rep[x]];
        }
        return x;
    }
    bool merge(int x, int y){
        x = find(x);
        y = find(y);
        if (x == y) return false;
        if (str[x].size() < str[y].size()) swap(x, y);
        str[x].insert(str[x].end(), str[y].begin(), str[y].end());
        str[y] = {};
        rep[y] = x;
        return true;
    }
    string smallestStringWithSwaps(string& s, vector<vector<int>>& pairs) {
        int N = s.size();
        rep.resize(N);
        iota(rep.begin(), rep.end(), 0);
        str.resize(N);
        for(int i = 0; i < N; ++i)str[i].push_back(s[i]);
        for(auto x: pairs){
            merge(x[0], x[1]);
        }
        for(int i = 0; i < N; ++i){
            if(rep[i] == i){
                sort(str[i].begin(), str[i].end(), greater());
            }
        }
        int p;
        for(int i = 0; i < N; ++i){
            p = find(i);
            s[i] = str[p].back(); str[p].pop_back();
        }
        return s;    
    }
};