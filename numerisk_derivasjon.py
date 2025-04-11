import numpy as np
h = 10**(-2)

x = 1.5

def df(h, x):
    return (np.exp(x+h)-np.exp(x))/h
resultat = df(h,x)
print(resultat)

def d2f(h,x):
    return(np.exp(x+h)-np.exp(x-h))/(2*h)
resultat2 = d2f(h,x)
print(resultat2)

def f(x,h):

    return (np.exp(x-2*h)-8*np.exp(x-h)+8*np.exp(x+h)-np.exp(x+2*h))/(12*h)
resultat3 = f(x,h)
print (resultat3)
    