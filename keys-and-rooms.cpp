class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        queue<int> q; q.push(0);
        vector<int> visited(rooms.size(), false);
        visited[0] = true;
        int v;
        while(!q.empty()){
            v = q.front(); q.pop();
            for(const auto& ch: rooms[v]){
                if(!visited[ch]){
                    visited[ch] = true;
                    q.push(ch);
                }
            }
        }
        return find(visited.begin(), visited.end(), false) == visited.end();
    }
};