from itertools import permutations
a=679
n=list(str(a))
num1=sorted(n)
perm=permutations(num1)
print(perm)
for i in perm:
    string = ""
    for j in i:
        string+=j
    print(string)

def primegenerator(n):
    primes=[True]*(n+1)
    primes[0]=False
    primes[1]=False
    for i in range(2,int(n**0.5)+1):
        if primes[i]==True:
            for x in range(i*i,n+1,i):
                primes[x]=False
    for i in range(len(primes)):
        if primes[i]==True:
            print(i,end=" ")
primegenerator(50)