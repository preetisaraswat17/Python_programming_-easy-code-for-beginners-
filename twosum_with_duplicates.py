def twosum(arr,sum):
    
 arr1=set(arr)
 arr=list(arr1)
 sums=[]

 for i in range(len(arr)):
        
   other_element=sum-arr[i]
   if other_element in arr:
     sums.append([arr[i], other_element])
   
 return sums
    
# keep this function call here  
print twosum([3, 5, 2, 4, 1, 3, 2, 8, 11], 7)