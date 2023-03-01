class NumMatrix {
public:
    vector <vector<int>> pre;
    NumMatrix(vector<vector<int>>& matrix) {
        vector <int> row_pre;
        pre.push_back(vector<int>(matrix[0].size() + 1));
        long sum_;
        for(auto r: matrix){
            row_pre.clear();
            row_pre.push_back(0);
            sum_ = 0;
            for(auto n: r){
                sum_ += n;
                row_pre.push_back(sum_);
            }
            pre.push_back(row_pre);
        }
        for(int c = 1; c <= matrix[0].size(); ++c){
            sum_ = 0;
            for(int r = 1; r <= matrix.size(); ++r){
                sum_ += pre[r][c];
                pre[r][c] = sum_;
            }
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        return pre[row2 + 1][col2 + 1] + pre[row1][col1] - pre[row2 + 1][col1] - pre[row1][col2 + 1];
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */