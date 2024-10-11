#Using heap
import heapq

def kth_largest(arr,k):
    
    arr = [-elem for elem in arr]
    
    heapq.heapify(arr)
    
    for i in range(k-1):
        
        heapq.heappop(arr)
        
    return -heapq.heappop(arr)



arr1 = [1,4,7,4,6,9,2,1,1,5]

k1 = 4

results = kth_largest(arr1,k1)

print(results)