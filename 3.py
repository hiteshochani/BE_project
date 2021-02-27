def my_function(arr, x):
    for i in range(len(n)):
        if arr[i]-x in n or x-arr[i] in n:
            print('Yes')
            break
    else:
        print('No')


t = int(input())
while t:
    a, b = map(int, input().split())
    arr = [int(x) for x in input().split()]
    my_function(arr, b)
    t=t-1