def p(x):
    return x>1 and all(x%i!=0 for i in range(2,int(x**0.5)+1))

def f(x):
    d=set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)
k=0
for n in range(5700001,7000000):
    d=[i for i in f(n) if p(i)]
    if len(d)>0:
        m=min(d)+max(d)
        if m>70000 and int(m**0.5)**2==m:
            print(n,m)
            k+=1
        if k==5:
            break
