class Solution {
public:
    int find_parent(int v){
        if(v == parent[v]) return v;
        parent[v] = find_parent(parent[v]);
        return parent[v];
    }
    void union_(int v, int u){
        int vpar = find_parent(v);
        int upar = find_parent(u);
        if(vpar == upar) return;
        if(len[vpar] < len[upar]) swap(vpar, upar);
        parent[upar] = vpar;
        len[vpar] += len[upar];
    }
    bool validPath(int n, vector<vector<int>>& edges, int src, int dst) {
        if(src == dst) return true;
        vector<int> check{src, dst};
        if(find(edges.begin(), edges.end(), check) != edges.end()) return true;
        check = {dst, src};
        if(find(edges.begin(), edges.end(), check) != edges.end()) return true;
        len.resize(n, 1);
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
        for(auto v: edges) union_(v[0], v[1]);
        return find_parent(src) == find_parent(dst);
    }
    vector<int> parent;
    vector<int> len;
};