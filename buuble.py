def bubble_sort(arr):
    max1=arr[0]
    max2=0
    for i in range(1,len(arr)):
        if arr[i]>max1:
            max2=max1
            max1=arr[i]
        else:
            if arr[i]>max2:
                max2=arr[i]
    print(arr)
    return max2

arr=[2,6,5,7,9]
print(bubble_sort(arr))
        