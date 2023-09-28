class Node{
    public:
        int pos;
        Node *child[26];
        Node(int i){
            pos = i;
            for(auto &ch: child) ch = nullptr;
        }
};

class Solution {
    Node* root;
    int N;
public:
    Solution(){
        root = new Node(-1);
    }

    bool insert(string s, string word){
        Node* cur = root;
        for(auto &ch: word){
            int idx = ch - 'a';
            if(cur->child[idx] == nullptr){
                cur->child[idx] = new Node((int)s.find(ch, cur->pos + 1));
            }
            if(cur->child[idx]->pos == -1) return false;
            cur = cur->child[idx];
        }
        return true;
    }

    int numMatchingSubseq(string s, vector<string>& words) {
        ios::sync_with_stdio(0);
        cin.tie(0);
        
        N = s.size();
        int ans = 0;
        for(auto &word: words){
            ans += insert(s, word);
        }
        return ans;
    }
};