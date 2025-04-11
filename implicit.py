import numpy as np
import matplotlib.pyplot as plt

# velger verdiar for h og k
h = 0.001
k = 0.015
x = np.arange(0,1+h,h)
t = np.arange(0,0.2+k,k)



n = len(x)
m = len(t)
T = np.zeros((n,m))
T[0,:] = 0
T[-1,:] = 0
T[:,0] = np.sin(x)
faktor = k/h**2

A = np.diag([1+2*faktor]*(n-2),0)+ np.diag([-faktor]*(n-3),-1)+ np.diag([-faktor]*(n-3),1)

for j in range(1,m):
    b = T[1:-1,j-1].copy()
    løysing = np.linalg.solve(A,b)
    T[1:-1,j] = løysing
    print (løysing)
    
print (b.round(3))
print (T.round(3))

R= np.linspace(1,0,m)
B = np.linspace(0,1,m)
G = 0
for j in range(m):
    plt.plot(x,T[:,j], color = [R[j],G,B[j]], label = round(t[j],3))

plt.xlabel('avstand')
plt.ylabel('temperatur')
plt.legend()
plt.show()





