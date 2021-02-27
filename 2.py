def insertion_sort(arr):
    a=[]
    a.append(arr[0])
    for i in range(1,len(arr)):
        for j in range(len(a)+1,0,-1):
            if j==0:
                if arr[i]>a[j]:
                    print(1)
                    a.append(arr[i])
                else:
                    a.append(a[j])
                    a[j]=arr[i]
            
            else:
                if arr[i] > a[j]:
                    print(1)
                    a.append(arr[i])
                else:
                    a.insert(j,arr[i])    
                    print(0)
    return a
    print(a)

arr=[7,6,4]
print(insertion_sort(arr))
