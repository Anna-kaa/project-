'''
def f(x,y):
    s=x//2
    if x<y:
        return 0
    if x==y:
        return 1
    else:
        return f(x-2,y)+f(int(x/2),y)
print(f(28,10)*f(10,1))
'''
def f(n, target):
    if n == target:
        return 1
    elif n < target:
        return 0
    else:
        return f(n-2, target) + f(n//2, target)

print(f(28, 10)*f(10,1))
