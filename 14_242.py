def f(s,n):
    a=''
    while s>0:
        a=str(s%n)+a
        s//=n
    return a
for n in range(1,36):
    if f(103,n)==f(97,n+2):
        print(n)
