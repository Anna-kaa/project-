def f(x):
    d=set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for n in range(1204300,1204381):
    d=[i for i in f(n) if i%2==0]
    s=sum(d)
    if s>0 and s%10==0:
        print(n,s)
