n=[1,2,3,4,5,6]
ps=[[]]
x=[]
for i in range(len(n)):
    ps+=[j+ [n[i]] for j in ps]

for i in ps:
   x.append(sum(i))

a=max(x)
x.remove(a)
b=max(x)
print(a-b)
