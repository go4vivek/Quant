#Calculate first and second derivatives in Python using finite difference method

def derivatives(f,x,h=0.0001):
    df=(f(x+h)-f(x-h)/2*h)
    ddf=(f(x+h)-2*f(x)+f(x-h))/(h**2)
    return df, ddf

# How to run this code
from math import sin
df,ddf=derivatives(sin,90)