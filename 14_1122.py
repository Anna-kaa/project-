for x in range(1000):
    s=36**17-6**x+71
    a=[]
    while s>0:
        a=[s%6]+a
        s//=6
    if sum(int(i)for i in a)==61:
        print(x)
