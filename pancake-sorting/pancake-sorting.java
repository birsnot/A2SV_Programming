class Solution {
    public List<Integer> pancakeSort(int[] arr) {
        int n = arr.length;
        Stack <Integer> list = new Stack<Integer>();
        for(int i = n-1; i >= 0; --i){
            list.push(arr[i]);
        }
        List <Integer> temp = new ArrayList<Integer>();
        List <Integer> ans = new ArrayList<Integer>();
        int k;
        for(int i = n; i > 0; --i){
            temp.clear();
            k = n - list.indexOf(i);
            if(k==i){
                continue;
            }
            if(k!=1){
                for(int j = k; j > 0; --j){
                    temp.add(list.pop());
                }
                for(int j = 0; j < k; ++j){
                    list.push(temp.get(j));
                }
                ans.add(k);
                temp.clear();
            }
            for(int j = i; j > 0; --j){
                temp.add(list.pop());
            }
            for(int j = 0; j < i; ++j){
                list.push(temp.get(j));
            }
            ans.add(i);
        }
        return ans;
    }
}
