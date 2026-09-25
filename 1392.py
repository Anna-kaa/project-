def f(x):
    d=set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)
k=0
for n in range(550_000,1_000_000):
    a=f(n)
    s=sum(a)
    h=len(a)
    if s>0 and h>0:
        g=s//h
        if g%31==13:
            print(n,g)
            k+=1
        if k==5:
            break
