def selection_sort(arr):
    for i in range(0,len(arr)):
        min=i
        for j in range(i,len(arr)): 
            if arr[j]<arr[min]:
                min=j
        temp=arr[i]
        arr[i]=arr[min]
        arr[min]=temp

arr=[6,5,4]
selection_sort(arr)
print(arr
      
123455
