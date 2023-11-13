
class DetectSquares {
public:
    unordered_map<int, unordered_map<int, int>> points;
    DetectSquares() {
    }
    
    void add(vector<int> point) {
        points[point[0]][point[1]]++;
    }
    
    int count(vector<int> point) {
        int ans = 0, x0 = point[0], y0 = point[1];
        for(auto &[x1, p]: points){
            for(auto &[y1, fq]: p){
                if(y1 != y0 && x0 == x1){
                    int s = y1 - y0;
                    ans += (points[x0 + s][y0]*points[x0 + s][y1] + points[x0 - s][y0]*points[x0 - s][y1])*fq;
                }
            }
        }
        return ans;
    }
};

/**
 * Your DetectSquares object will be instantiated and called as such:
 * DetectSquares* obj = new DetectSquares();
 * obj->add(point);
 * int param_2 = obj->count(point);
 */