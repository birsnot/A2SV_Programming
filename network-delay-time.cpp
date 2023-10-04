class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<pair<int, int>> graph[n];
        for(auto &edge: times){
            graph[edge[0] - 1].push_back({edge[1] - 1, edge[2]});
        }
        k--;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        pq.push({0, k});

        vector<bool> visited(n);
        vector<int> distance(n, INT_MAX);
        distance[k] = 0;
        
        while(!pq.empty()){
            auto [w, v] = pq.top(); pq.pop();
            if(visited[v]) continue;
            visited[v] = true;
            for(auto [ch, w2]: graph[v]){
                int cur_w = w + w2;
                if (distance[ch] > cur_w){
                    distance[ch] = cur_w;
                    pq.push({cur_w, ch});
                }
            }
        }
        int ans = *max_element(distance.begin(), distance.end());
        return ans == INT_MAX ? -1 : ans;
    }
};