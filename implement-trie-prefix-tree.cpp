class Node {
public:
    Node *child[26];
    bool isEnd;
    Node(): isEnd(false){
        for(auto &ch: child) ch = nullptr;
    }
};

class Trie {
    Node *root;
public:
    Trie() {
        root = new Node();
    }
    
    void insert(string word) {
        Node *cur = root;
        for(auto ch: word){
            int idx = ch - 'a';
            if(!cur->child[idx]){
                cur->child[idx] = new Node();
            }
            cur = cur->child[idx];
        }
        cur->isEnd = true;
    }
    
    bool search(string word) {
        Node *cur = root;
        for(auto ch: word){
            int idx = ch - 'a';
            if(!cur->child[idx]){
                return false;
            }
            cur = cur->child[idx];
        }
        return cur->isEnd;
    }
    
    bool startsWith(string prefix) {
        Node *cur = root;
        for(auto ch: prefix){
            int idx = ch - 'a';
            if(!cur->child[idx]){
                return false;
            }
            cur = cur->child[idx];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */