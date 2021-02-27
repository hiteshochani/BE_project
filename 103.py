from itertools import product
x,y=map(int,input().split())
n=int(input())
count=0
a=[]
dict={}
for i in range(x,y+1):
    a.append(i)
c=list(product(a,repeat=n))
for i in c:
    if str(0) in i:
        pass
    else:
        s=sum(i)
        if s>0 and s%2==0:
            count+=1
print(count)
        