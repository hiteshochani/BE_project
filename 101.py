a=1000000
b=2235959
count=0
y={}
for i in range(a,b+1):
    x=str(i)
    if int(x[-2:])>59 or int(x[-4:-2])>59 or int(x[-6:-4])>23:
        pass
    else:
        y.update({x:1})
for i in y:
    z=i[::-1]
    if int(z[-2:]) > 59 or int(z[-4:-2]) > 59 or int(z[-6:-4]) > 23 or int(z[1])>int(str(b)[1]):
        pass
    else:
        if a<=int(z[::-1])<=b:
            count+=1
              
print(count)
    
