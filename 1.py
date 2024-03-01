a={"restart": 1, "laptop": 2, "install":3, "smartphone":4, "hardware":5, "mouse":6}
x=input()
l=0
n=len(a)
r=n-1
m=n//2
a=dict(sorted(a.items()))
keys=list(a.keys())
values=list(a.values())
print(*keys)
while(l<=r):
    if x<keys[m]:
        r=m-1
    elif x>keys[m]:
        l=m+1
    elif x==keys[m]:
        print(f"Позиція до сортування: {values[m]}\nПозиція після сортування: {m}")
        break
    m=(r+l)//2

if(l>r):
    print("Такого терміну немає в масиві")