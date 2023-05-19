class Solution {
public:
    int openLock(vector<string>& deadends, string t) {
        ios::sync_with_stdio(0);
        cin.tie(0);
        if(find(deadends.begin(), deadends.end(), "0000") != deadends.end()) return -1;
        unordered_set<int> visited;
        for(const auto& d: deadends)
            visited.insert(stoi(d));
        queue<int> q;
        q.push(0);
        visited.insert(0);
        int ans = 0, len, target = stoi(t), temp, cur;
        int tens[] = {10, 100, 1000, 10000};
        while(!q.empty()){
            len = q.size();
            for(int i = 0; i < len; ++i){
                cur = q.front(); q.pop();
                if(cur == target) return ans;
                for(int j = 0; j < 4; ++j){
                    temp = (cur/tens[j])*tens[j] + (cur%tens[j] + tens[j]/10)%tens[j];
                    if(!visited.count(temp)) {
                        visited.insert(temp);
                        q.push(temp);
                    }
                    temp = (cur/tens[j])*tens[j] + (cur%tens[j] - tens[j]/10 + tens[j])%tens[j];
                    if(!visited.count(temp)) {
                        visited.insert(temp);
                        q.push(temp);
                    }
                }
            }
            ++ans;
        }
        return -1;
    }
};