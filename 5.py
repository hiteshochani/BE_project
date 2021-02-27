no=int(input())
b=[int(i) for i in input().split()]
c=[]
for i in range(len(b)):
    for j in range(i+1,len(b)):
        if b[i]<b[j]:
            b.remove(b[i])
            b.remove(b[j])
            c.append(b[i])
            break
print(b)
print(c)
print(len(c))


    