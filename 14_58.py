s=64**30+2**300-4
k=0
while s:
    if s%8==7:
        k+=1
    s//=8
print(k)
