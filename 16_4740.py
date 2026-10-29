import sys
sys.setrecursionlimit(5100)

import math

def f(n):
    if n>=5000:
        return math.factorial(n)
    if 1<=n<5000:
        return 2*f(n+1)//(n+1)
print(1000*f(7)//f(4))
