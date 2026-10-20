def f(x):
    d=set()
    for i in range(2,int(x**0.5)):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)
k=0
for n in range(400_000_000,1_000_000_000):
    d=f(n)
    if len(d)>=5:
        p=d[0]*d[1]*d[2]*d[3]*d[4]
        if p%100==17 and p<n:
            print(p,d[4])
            k+=1
        if k==5:
            break
