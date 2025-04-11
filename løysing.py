import numpy as np
import matplotlib.pyplot as plt

def An(n):
    return (np.sin((1-n*np.pi)*1)/(1-n*np.pi)-np.sin((1+n*np.pi)*1)/(1+n*np.pi))-(1/2*(np.sin((1-n*np.pi)*0)/(1-n*np.pi)-np.sin((1+n*np.pi)*0)/(1+n*np.pi)))

import numpy as np
import matplotlib.pyplot as plt


h = 0.001
k = 0.015
x = np.arange(0,1+h,h)
t = np.arange(0,0.2+k,k)

initialkrav = np.sin(x)

n = len (x)
m = len(t)

T2 = np.zeros((n,m))
T2[:,0] = initialkrav


def u(x,t):
    resultat = 0
    for w in range(10):
        resultat += An(w)*np.sin(w*np.pi*x)*np.exp(-(w*np.pi)**2*t)
    return resultat

for j in range(1,m):
    for i in range (1,n-1):
        T2[i,j] = u(i*h,j*k)
T2[:,0] = initialkrav
        
R= np.linspace(1,0,m)
B = np.linspace(0,1,m)
G = 0


for j in range(m):
    plt.plot(x,T2[:,j], color = [R[j],G,B[j]], label = round(t[j],3))

plt.xlabel('avstand')
plt.ylabel('tempratur')
plt.legend()
plt.show()


                                                            





