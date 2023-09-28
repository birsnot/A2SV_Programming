class Solution {
public:
    class TrieNode{
        public:
        TrieNode *bit[2];
        TrieNode(){
            bit[0] = bit[1] = nullptr;
        }
    };
    void insert(int num){
        TrieNode *cur = root;
        bool idx;
        for(int i = 30; i >= 0; --i){
            idx = ((num&(1<<i)) > 0);
            if(cur->bit[idx] == nullptr) cur->bit[idx] = new TrieNode();
            cur = cur->bit[idx];
        }
    }

    int find(int num){
        TrieNode *cur = root;
        bool idx;
        int ans = 0;
        for(int i = 30; i >= 0; --i){
            idx = ((num&(1<<i)) == 0);
            if(cur->bit[idx] == nullptr) idx ^= 1;
            else ans |= 1<<i;
            cur = cur->bit[idx];
        }
        return ans;
    }

    int findMaximumXOR(vector<int>& nums) {
        root = new TrieNode();
        int ans = 0;
        for(auto &num: nums){
            insert(num);
            ans = max(ans, find(num));
        }
        return ans;
    }

    TrieNode *root;
};