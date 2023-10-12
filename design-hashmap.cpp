int hashmap[1000005];

class MyHashMap {
public:
    MyHashMap() {
        memset(hashmap, -1, sizeof hashmap);
    }
    
    void put(int key, int value) {
        hashmap[key] = value;
    }
    
    int get(int key) {
        return hashmap[key];
    }
    
    void remove(int key) {
        hashmap[key] = -1;
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */