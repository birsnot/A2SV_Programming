class Node{
    public:
        int sum, val;
        Node *child[26];
        Node(){
            sum = val = 0;
            for(auto &ch: child) ch = nullptr;
        }
};

class MapSum {
    Node *root;
public:
    MapSum() {
        root = new Node();
    }
    
    void insert(string key, int val) {
        int net = val - getVal(key);
        insert(key, val, net);
    }

    void insert(string key, int val, int net){
        Node *cur = root;
        for(auto &ch: key){
            int idx = ch - 'a';
            if(cur->child[idx] == nullptr){
                cur->child[idx] = new Node();
            }
            cur = cur->child[idx];
            cur->sum += net;
        }
        cur->val = val;
    }

    int getVal(string key){
        Node *cur = root;
        for(auto &ch: key){
            int idx = ch - 'a';
            if(cur->child[idx] == nullptr) return 0;
            cur = cur->child[idx];
        }
        return cur->val;
    }
    
    int sum(string prefix) {
        Node *cur = root;
        for(auto &ch: prefix){
            int idx = ch - 'a';
            if(cur->child[idx] == nullptr) return 0;
            cur = cur->child[idx];;
        }
        return cur->sum;
    }
};

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum* obj = new MapSum();
 * obj->insert(key,val);
 * int param_2 = obj->sum(prefix);
 */