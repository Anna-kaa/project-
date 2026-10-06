def f(x):
    d=set()
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)
for n in range(154026,154044):
    s=f(n)
    if len(s)==4:
        print(s[-2],s[-1])
        
