class KthLargest {
public:
    priority_queue<int, vector<int>, greater<>> minq;
    int K;
    KthLargest(int k, vector<int>& nums): minq(nums.begin(), nums.end()), K(k) {
        while(minq.size() > k) minq.pop();
    }
    
    int add(int val) {
        minq.push(val);
        if(minq.size() > K) minq.pop();
        return minq.top();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */