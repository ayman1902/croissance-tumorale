import matplotlib.pyplot as plt
import math as mt
plt.style.use('seaborn')
#plt.style.use('dark_background')
def gompertz_verhulst_expo(no,p,a,b,dub,fin):
    pas=(fin-dub)/p
    
    T=[dub]
    g=[no]
    v=[no]
    #exp=[no]
    for i in range(1,p+1):
        T.append(dub+pas*i)
        nig=g[len(g)-1]
        niv=v[len(v)-1]
        #niexp=exp[len(exp)-1]
        neg=(nig+pas*a*mt.log(b/nig)*nig)
        nev=(niv+pas*a*niv*(1-(niv/b)))
        #neexp=(niexp + (a)*pas*niexp)
        g.append(neg)
        v.append(nev)
        #exp.append(neexp)
    plt.plot(T,g,label='Gompertz')
    plt.plot(T,v,label='Verhulst')
    #plt.plot(T,exp,label='Malthus')
    plt.title('No=100 , a=0.15 , b =10**4 , T=40')
    plt.xlabel('Jour')
    plt.ylabel('Cellules tumorales')
    plt.legend()
    plt.show()
gompertz_verhulst_expo(7,100,0.15,10**(5),0,300)