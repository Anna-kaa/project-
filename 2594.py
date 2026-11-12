def f(x):
    d=set()
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)
for n in range(113_000_000,114_000_001):
    d=[i for i in f(n) if i%2==0]
    if len(d)==3:
        print(n,d[1])
        
