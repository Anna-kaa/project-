def f(x):
    d=set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)
k=0
for n in range(150000,1000000):
    s=sum(f(n))
    if s%13==10:
        print(n,s)
        k+=1
    if k==7:
        break
