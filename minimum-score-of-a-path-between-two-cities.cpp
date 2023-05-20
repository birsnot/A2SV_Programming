class Solution {
public:
    vector<int> parent;

    int find(int v){
        while(v != parent[v]) v = parent[v];
        return v;
    }
    int minScore(int n, vector<vector<int>>& roads) {
        ios::sync_with_stdio(0);
        cin.tie(0);
        parent.resize(n + 1);
        vector<int> score(n + 1, INT_MAX);
        iota(parent.begin(), parent.end(), 0);
        for(auto road: roads){
            int xpar = find(road[0]);
            int ypar = find(road[1]);
            if(xpar > ypar) swap(xpar, ypar);
            parent[ypar] = xpar;
            score[xpar] = min(score[xpar], min(score[ypar], road[2]));
        }
        return score[1];
    }
};