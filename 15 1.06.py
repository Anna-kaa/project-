def f(x,y,A):
    return (x>=27)or(2*x<3*y)or(A>(x+2)*(y-3))
for A in range(0,1000):
    if all(f(x,y,A)for x in range(0,1000)for y in range(0,1000)):
        print(A)
        break
