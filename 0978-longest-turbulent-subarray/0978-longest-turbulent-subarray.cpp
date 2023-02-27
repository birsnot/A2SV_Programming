class Solution {
public:
    int maxTurbulenceSize(vector<int>& arr) {
        char sign = '=';
        int count = 1, ans = 1, N = arr.size() - 1;
        for (int i = 0; i < N; ++i){
            if (sign == '<'){
                if(arr[i] < arr[i+1]){
                    ++count;
                    sign = '>';
                }
                else{
                    ans = max(ans, count);
                    count = 1;
                    if (arr[i] == arr[i+1]) sign = '=';
                    else count += 1;
                }
            }
            else if (sign == '>'){
                if(arr[i] > arr[i+1]){
                    ++count;
                    sign = '<';
                }
                else{
                    ans = max(ans, count);
                    count = 1;
                    if(arr[i] == arr[i+1]) sign = '=';
                    else count += 1;
                }
            }
            else {
                count = 2;
                if(arr[i] < arr[i+1]){
                    sign = '>';
                }
                else if (arr[i] > arr[i+1]){
                    sign = '<';
                }
                else{
                    sign = '=';
                    count = 1;
                }
            }
        }
        return max(ans, count);
    }
};