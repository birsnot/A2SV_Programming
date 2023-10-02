class Node{
    public:
        int cnt;
        Node* child[26];
        Node(){
            cnt = 0;
            for(auto &ch: child) ch = nullptr;
        }
};

class Solution {
    Node* root;
public:
    Solution(){
        root = new Node();
    }

    void insert(string &word){
        Node *cur = root;
        int idx;
        for(auto ch: word){
            idx = ch - 'a';
            if(cur->child[idx] == nullptr) cur->child[idx] = new Node();
            cur = cur->child[idx];
            cur->cnt++;
        }
    }

    int get_cnt(string &word){
        Node *cur = root;
        int ans = 0;
        for(auto ch: word){
            cur = cur->child[ch - 'a'];
            ans += cur->cnt;
        }
        return ans;
    }

    vector<int> sumPrefixScores(vector<string>& words) {
        for(auto &word: words) insert(word);
        vector<int> ans(words.size());
        for(int i = 0; i < words.size(); ++i) ans[i] = get_cnt(words[i]);
        return ans;
    }
};