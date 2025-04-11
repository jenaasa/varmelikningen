import  numpy as np
import matplotlib.pyplot as plt

# velger verdiar for h og k
h = 0.05
k = 0.0008
x  = np.arange(0, 1+h,h)
t = np.arange(0, 0.2+k,k)

n = len(x)
m = len(t)
#lagar ei matrise der antall punkt i tid blir representer i antall kolonner og antall punkt i x blir antall rader.
#setter så første og siste rad til 0, og første kolonne til initialfunksjonen.
T = np.zeros((n,m))
T[-1,:] = 0
T[0,:] = 0
T[:,0] = np.sin(x)


faktor = k/h**2

# går så gjennom kvart av punkta og løyser med den eksplisitte formelen.
for j in range(1,m):
    for i in range(1,n-1):
        T[i,j]=faktor*T[i-1,j-1]+ (1-2*faktor)*T[i,j-1]+ faktor*T[i+1,j-1]

for j in range(m):
    R= np.linspace(1,0,m)
    B = np.linspace(0,1,m)
    G = 0
    plt.plot(x,T[:,j], color = [R[j],G,B[j]], label = round(t[j],3))
#plt.plot(T)
#plt.legend(t)
plt.xlabel("avstand")
plt.ylabel("temperatur")
plt.show()

