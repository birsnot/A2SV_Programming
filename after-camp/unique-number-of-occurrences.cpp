class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> cnt;
        for(auto n: arr) cnt[n]++;
        unordered_set<int> fqs;
        for(auto &[_, fq]: cnt){
            fqs.insert(fq);
        }
        return fqs.size() == cnt.size();
    }
};