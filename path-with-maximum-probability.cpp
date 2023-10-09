class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start_node, int end_node) {
        vector<pair<int, double>> graph[n];
        for(int i = 0; i < edges.size(); ++i){
            graph[edges[i][0]].push_back({edges[i][1], succProb[i]});
            graph[edges[i][1]].push_back({edges[i][0], succProb[i]});
        }

        priority_queue<pair<double, int>> pq;
        vector<double> prob(n);
        vector<bool> visited(n);
        prob[start_node] = 1;
        pq.push({1, start_node});
        while(!pq.empty()){
            auto [p, v] = pq.top(); pq.pop();
            if(v == end_node) return p;
            if(visited[v]) continue;

            for(auto [ch, w]: graph[v]){
                double new_p = w*p;
                if (new_p > prob[ch] && !visited[ch]){
                    prob[ch] = new_p;
                    pq.push({new_p, ch});
                }
            }
        }
        return 0;
    }
};