import numpy as np
import matplotlib.pyplot as plt

h = 0.1
k = 0.05
h = 0.1
k = 0.025
h = 0.001
k = 0.015
x = np.arange(0,1+h,h)
t = np.arange(0,0.2+k,k)



n = len (x)
m = len(t)
#lagar ei matrise der antall punkt i tid blir representer i antall kolonner og antall punkt i x blir antall rader.
#setter så første og siste rad til 0, og første kolonne til initialfunksjonen.
T = np.zeros((n,m))
T[0,:] = 0
T[-1,:] = 0
T[:,0] = np.sin(x)





faktor = k/h**2
#Setter opp dei to matrisene som ingår i likningsystmet. np.diag plaserer elementet [2+2*faktor] langs ein diagonal
#som er n-2 lang. np.diag([-faktor]*(n-3),-1) plaserer -faktor n-3 ganger på diagonalen under diagonalen.
A = np.diag([2+2*faktor]*(n-2),0) + np.diag([-faktor]*(n-3),-1)+ np.diag([-faktor]*(n-3),1)
B = np.diag([2-2*faktor]*(n-2),0) + np.diag([faktor]*(n-3),-1) + np.diag([faktor]*(n-3),1)

for j in range(0,m-1):
    b = T[1:-1,j].copy()
    # tar prikkproduktet mellom matrisa B og kollona ved tidspunktet j.
    b = np.dot(B,b)
    b[0] = b[0] + faktor*(T[0,j]+ T[0,j+1])
    b[-1] = b[-1] + faktor*(T[-1,j] + T[-1,j+1])
    #bruker til å løyse likningsystemet og få den neste kolonna i matrisa.
    løysing = np.linalg.solve(A,b)
    #legger til kolonna i matrisa. 
    T[1:-1,j+1] = løysing
R= np.linspace(1,0,m)
B = np.linspace(0,1,m)
G = 0
for j in range(m):
    plt.plot(x,T[:,j], color = [R[j],G,B[j]], label = round(t[j],3))

plt.xlabel('avstand')
plt.ylabel('tempratur')
plt.legend()
plt.show()


                                                            





