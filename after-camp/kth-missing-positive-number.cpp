class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int l = 0, r = arr.size() - 1, mid;
        while(l <= r){
            mid = l + (r - l)/2;
            if(arr[mid] - mid - 1 >= k) r = mid - 1;
            else l = mid + 1;
        }
        return r + 1 + k;
    }
};