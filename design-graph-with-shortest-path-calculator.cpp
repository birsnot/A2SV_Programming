int dis[100][100];
class Graph {
public:
    int n;
    Graph(int n, vector<vector<int>>& edges) {
        this->n = n;
        for(int i = 0; i < n; ++i){
            fill(dis[i], dis[i] + n, 1e9);
            dis[i][i] = 0;
        }
        for(auto &edge: edges){
            dis[edge[0]][edge[1]] = edge[2];
        }
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < n; ++j){
                for(int k = 0; k < n; ++k){
                    dis[j][k] = min(dis[j][k], dis[j][i] + dis[i][k]);
                }
            }
        }
    }
    
    void addEdge(vector<int> edge) {
        int u = edge[0], v = edge[1], c = edge[2];
        if(dis[u][v] > c){
            dis[u][v] = c;
            for(int i = 0; i < n; ++i){
                for(int j = 0; j < n; ++j){
                    dis[i][j] = min(dis[i][j], dis[i][u] + dis[v][j] + c);
                }
            }
        }
    }
    
    int shortestPath(int node1, int node2) {
        return dis[node1][node2] == 1e9 ? -1 : dis[node1][node2];
    }
};

/**
 * Your Graph object will be instantiated and called as such:
 * Graph* obj = new Graph(n, edges);
 * obj->addEdge(edge);
 * int param_2 = obj->shortestPath(node1,node2);
 */