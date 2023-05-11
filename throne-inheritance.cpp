class ThroneInheritance {
public:
    ThroneInheritance(string kingName) {
        this->kingName = kingName;
    }
    
    void birth(string parentName, string childName) {
        children[parentName].push_back(childName);
    }
    
    void death(string name) {
        dead.insert(name);
    }
    
    vector<string> getInheritanceOrder() {
        vector<string> order;
        dfs(kingName, order);
        return order;
    }
private:
    string kingName;
    unordered_map<string, vector<string>> children;
    unordered_set<string> dead;
    void dfs(string v, vector<string>& order){
        if(!dead.count(v)) order.push_back(v);
        if(!children.count(v)) return;
        for(string ch: children[v]){
            dfs(ch, order);
        }
    }
};

/**
 * Your ThroneInheritance object will be instantiated and called as such:
 * ThroneInheritance* obj = new ThroneInheritance(kingName);
 * obj->birth(parentName,childName);
 * obj->death(name);
 * vector<string> param_3 = obj->getInheritanceOrder();
 */