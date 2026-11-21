from turtle import*
screensize(5000,5000)
tracer(0)
r=20
for i in range(36):
    rt(60)
    fd(1*r)
    rt(60)
    fd(1*r)
    rt(270)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*r,y*r)
        dot(3,'red')
done()
