class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> cnt;
        for(const auto& word: words) ++cnt[word];
        struct mycmp {
            bool operator()(const pair<int, string>& a, const pair<int, string>& b) const{
                if(a.first == b.first) return a.second > b.second;
                return a.first < b.first;
            }
        };
        priority_queue<pair<int, string>, vector<pair<int, string>>, mycmp> pq;
        for(auto c: cnt){
            pq.push({c.second, c.first});
        }
        vector<string> ans;
        for(int i = 0; i < k; ++i){
            ans.push_back(pq.top().second); pq.pop();
        }
        return ans;
    }
};