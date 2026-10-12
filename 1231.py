def f(x):
    d=set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)
k=0
for n in range(250200,10**6):
    s=f(n)
    if len(s)>=2:
        c=min(s)+max(s)
        if c%123==17:
            print(n,c)
            k+=1
        if k==5:
            break
    
