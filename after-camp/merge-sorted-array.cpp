class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int p1 = m - 1, p2 = n - 1, i = n + m - 1;
        while(p2 >= 0 && p1 >= 0){
            if(nums2[p2] >= nums1[p1]) nums1[i--] = nums2[p2--];
            else nums1[i--] = nums1[p1--];
        }
        while(p2 >= 0) nums1[i--] = nums2[p2--];
    }
};