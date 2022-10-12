#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        return min(arr[i:])
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            selection = self.select(arr,i)
            selection_index = arr[i:].index(selection)
            arr[i + selection_index] = arr[i]
            arr[i] = selection
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
