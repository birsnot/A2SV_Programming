class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<array<int, 2>> adj[n];
        for(auto edge: flights){
            adj[edge[0]].push_back({edge[1], edge[2]});
        }

        priority_queue<array<int, 3>, vector<array<int, 3>>, greater<array<int, 3>>> pq;
        pq.push({0, 0, src});

        vector<int> visited(n, k + 1);

        while(!pq.empty()){
            auto [w, stops, v] = pq.top(); pq.pop();
            if(v == dst) return w;
            if(visited[v] <= stops) continue;
            visited[v] = stops++;
            for(auto [ch, w2]: adj[v]){
                pq.push({w + w2, stops, ch});
            }
        }
        return -1;
    }
};