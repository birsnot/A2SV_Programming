class Node {
    public:
        Node *child[26];
        bool isEnd;
        Node(){
            isEnd = false;
            for(auto &ch: child) ch = nullptr;
        }
};

class WordDictionary {
    Node *root;
public:
    WordDictionary() {
        root = new Node();
    }
    
    void addWord(string word) {
        Node* cur = root;
        for(auto &ch: word){
            int idx = ch - 'a';
            if(cur->child[idx] == nullptr){
                cur->child[idx] = new Node();
            }
            cur = cur->child[idx];
        }
        cur->isEnd = true;
    }
    
    bool search(string word) {
        return search(word, root);
    }
    bool search(string word, Node *cur){
        for(int j = 0; j < word.size(); ++j){
            char ch = word[j];
            if(ch == '.'){
                for(int i = 0; i < 26; ++i){
                    if(cur->child[i] != nullptr && search(word.substr(j + 1), cur->child[i])) return true;
                }
                return false;
            }
            int idx = ch - 'a';
            if(cur->child[idx] == nullptr) return false;
            cur = cur->child[idx];
        }
        return cur->isEnd;
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */