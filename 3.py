from random import randint
n=9
a=[]
for i in range(n):
    x=randint(7, 21)
    a.append(x)
r=n-1
print(*a)
while r>0:
    p=True
    for i in range(n-1):
        if a[i]<a[i+1]:
            z=a[i]
            a[i]=a[i+1]
            a[i+1]=z
            p=False
    if p:
        break
    r-=1
print(*a)
    