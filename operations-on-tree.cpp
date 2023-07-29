class LockingTree {
    vector<int> parent;
    vector<vector<int>> child;
    vector<int> locked;
    int N;
public:
    LockingTree(vector<int>& parent) {
        this->parent = parent;
        N = parent.size();
        locked.resize(N);
        child.resize(N,vector<int>());
        for(int i = 1; i < N; ++i){
            child[parent[i]].push_back(i);
        }
    }
    
    bool lock(int num, int user) {
        if(locked[num]) return false;
        locked[num] = user;
        return true;
    }
    
    bool unlock(int num, int user) {
        if(locked[num] != user) return false;
        locked[num] = 0;
        return true;
    }
    
    bool upgrade(int num, int user) {
        int p = num;
        while(p != -1){
            if(locked[p]) return false;
            p = parent[p];
        }
        if(!check_child(num)) return false;
        locked[num] = user;
        return true;
    }
    bool check_child(int num){
        bool ret = false;
        for(auto ch: child[num]){
            if(locked[ch]){
                ret = true;
                locked[ch] = 0;
            }
            ret = check_child(ch) || ret;
        }
        return ret;
    }
};

/**
 * Your LockingTree object will be instantiated and called as such:
 * LockingTree* obj = new LockingTree(parent);
 * bool param_1 = obj->lock(num,user);
 * bool param_2 = obj->unlock(num,user);
 * bool param_3 = obj->upgrade(num,user);
 */