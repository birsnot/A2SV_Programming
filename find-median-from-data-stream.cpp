class MedianFinder {
    priority_queue<int> maxHeap;
    priority_queue<int, vector<int>, greater<>> minHeap;
public:
    MedianFinder() {
        maxHeap.push(-1e6);
        ios::sync_with_stdio(0);
        cin.tie(0);
    }
    
    void addNum(int num) {
        if(num <= maxHeap.top()){
            if(maxHeap.size() > minHeap.size()){
                maxHeap.push(num);
                minHeap.push(maxHeap.top());
                maxHeap.pop();
            }
            else maxHeap.push(num);
        }
        else{
            if(minHeap.size() == maxHeap.size()){
                minHeap.push(num);
                maxHeap.push(minHeap.top());
                minHeap.pop();
            }
            else minHeap.push(num);
        }
    }
    
    double findMedian() {
        if (minHeap.size() == maxHeap.size()) return minHeap.top();
        else {
            double n1 = minHeap.top(), n2 = maxHeap.top();
            return (n1 + n2)/2;
        }
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */