def twosum(arr,sum):
    
 sums=[]

 for i in range(len(arr)):
        
   other_element=sum-arr[i]
   if other_element in arr:
     sums.append([arr[i], other_element])
 return sums
    
# keep this function call here  
print twosum([3, 5, 2, 4, 8, 11], 7)
  