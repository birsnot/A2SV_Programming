class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        p = i
        while True:
            left = 2*p + 1
            right = left + 1
            if right < n and arr[right] > arr[left]:
                if arr[right] > arr[p]:
                    arr[p], arr[right] = arr[right], arr[p]
                    p = right
                else:
                    break
            elif left < n and arr[left] > arr[p]:
                arr[p], arr[left] = arr[left], arr[p]
                p = left
            else:
                break
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        i = (n-2)//2
        while i >= 0:
            self.heapify(arr, n, i)
            i -=1
        
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        for i in range(n-1,0,-1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)
