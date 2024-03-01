a=[33, 17, 7, 45, 13, 21]
n=len(a)
for i in range(1, n):
    x=a[i]
    j=i-1
    while j>=0 and x<a[j]:
        a[j+1]=a[j]
        j-=1
    a[j+1]=x
print(*a)