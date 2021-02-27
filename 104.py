n,w,d=map(int,input().split())
arr=[int(i) for i in input().split()]
a=sum(arr[:w])
print(a\)
b=sum(arr[w+1:(w+1)+w-d])
b1=[b]
for i in range(2*w-d-1,n,w-d):
    sum+=arr[i]-arr[i-w-d]
    b1.append(sum)
print(a-max(b1))
                                       