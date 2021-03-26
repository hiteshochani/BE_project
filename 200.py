n=int(input())
names=[]
heights=[]
y=[]
i=True
CHANGES DONE
while i:
    s=input()
    if s=='q' or s=='Q':
        i=False 
    else:
        names.append(s)

for i in range(len(names)):
    x=float(input())
    heights.append(x)
    y.append(x)

heights.sort(reverse=True)
for i in range(n):
    index1 = y.index(heights[i])
    print(heights[i],names[index1])

