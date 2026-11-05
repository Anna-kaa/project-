for x in range(1000):
    s=125**200-5**x+74
    a=''
    while s>0:
        a=str(s%5)+a
        s//=5
    if a.count('4')==100:
        print(x)
