from cProfile import label
import math as mt
import numpy as np
from matplotlib import projections
import matplotlib.pyplot as plt
from pylab import cm
from mpl_toolkits import mplot3d
plt.style.use('seaborn')
#plt.style.use('dark_background')
def finite_differnce(a,ti,tf,k,d,No,n,p):
    #il ne faut pas prendre ti = 0 !!!
    #a: rayon de la tumeur
    #ti: temps initiale
    #tf:temps finale
    #k:parametre de proliferation
    #d:parametre de diffusion
    #No:nombre de cellules tumorale initiales
    #n:intervalles de temps
    #p:intervalles de l'espace
    
    ax = plt.gca()
    
    second=0.001
    dt = (tf-ti)/n
    dx = (2*a)/p
    
    #paramaetre de la shema numerique
    A=(d*dt)/(dx**2)
    B=(k*dt + 1 - 2*A)
    
    #dt et dx discretisation d'espace temps
    X=[-a+dx*i for i in range(0,p+1)]
    T=[ti+dt*j for j in range(0,n+1)]
    #condition initiales (x,ti)
    f = lambda x,t:(No/(4*mt.pi*d*t))*mt.exp(k*t)*mt.exp((-x**2)/(4*d*t))
    
    #premier etape collecte la premiere ligne la condition initiales c(x,ti)
    lavant=[f(x,ti) for x in X]
    lnatruel=[f(x,tf) for x in X]
    #simulation
    Xs=np.array(X)
    Ts=np.array(T)
    
    #line,=plt.plot(Xs,lavant,color='black')
    #line1,=plt.plot(Xs,lnatruel,color='orange',label='Analytique')
    #plt.title(' A = '+str(A))
    #plt.pause(1.3)
    #ax.lines.remove(line)
    
    
    #print(A,B)
    
    #algorithme ftcs
    M=[]#la matrice graphique
    M.append(lavant)#ajouter la premiere ligne
    
    lapres=[0]*(p+1)
    for j in range(1,n+1):#lignes par lignes
        #condition au bord
        lapres[0]=0
        lapres[p]=0
        for i in range(1,p):#domaine vierge
            lapres[i]=A*lavant[i+1]+B*lavant[i]+A*lavant[i-1]
        M.append(lapres)
        #line,=plt.plot(Xs,lapres,color='red')
        plt.title('T = '+str(ti+(j+1)*dt)+'jour'+ ' R= '+str(a)+'cm' +' k = '+str(k) + ' d = '+str(d) + ' No = '+ str(No)+' A = '+str(A))
        #plt.pause(second)
        '''if j !=n-1:
            ax.lines.remove(line)'''
        lavant,lapres=lapres,[0]*(p+1)
    #line,=plt.plot(Xs,M[-1],color='c',label='numérique')
    #ploting
    """Z=np.array(M)
    fig = plt.figure()
    ax = fig.gca(projection ="3d")
    Xs2,Ts2=np.meshgrid(Xs,Ts)
    surf=ax.plot_surface(Xs2,Ts2,Z)"""   
    plt.plot(Xs,M[n-1])
    #return M[n-1]
    plt.legend()
    plt.show()
def mesure_stabilite(a,ti,tf,k,d,No,n,p1,p2):
    X=[i for i in range(p1,p2+1)]
    para=[(d*(tf-ti)/n)/(((2*a)/i)**2) for i in X]
    Y=[]
    l=[]
    for i in X:
        l=finite_differnce(a,ti,tf,k,d,No,n,i)
        norme=max([abs(l[j+1]-l[j]) for j in range(len(l)-1)])
        print((d*(tf-ti)/n)/(((2*a)/i)**2),norme)
        Y.append(mt.log(norme))
        l=[]
    plt.xlabel('A')
    plt.ylabel('Ecart')
    plt.plot(para,Y)
    plt.show()
def finite_differnce_3d(a,ti,tf,k,d,No,n,p):
    #il ne faut pas prendre ti = 0 !!!
    #a: rayon de la tumeur
    #ti: temps initiale
    #tf:temps finale
    #k:parametre de proliferation
    #d:parametre de diffusion
    #No:nombre de cellules tumorale initiales
    #n:intervalles de temps
    #p:intervalles de l'espace
    
    
    
    second=0.01
    dt = (tf-ti)/n
    dx = (2*a)/p
    #dt et dx discretisation d'espace temps
    X=[-a+dx*i for i in range(0,p+1)]
    T=[ti+dt*j for j in range(0,n+1)]
    #condition initiales (x,ti)
    f = lambda x:(No/(4*mt.pi*d*ti))*mt.exp(k*ti)*mt.exp((-x**2)/(4*d*ti))
    #premier etape collecte la premiere ligne la condition initiales c(x,ti)
    lavant=[f(x) for x in X]
    
    #simulation
    Xs=np.array(X)
    Ts=np.array(T)
    
    
    #paramaetre de la shema numerique
    A=(d*dt)/(dx**2)
    B=(k*dt + 1 - 2*A)
    #print(A,B)
    
    #algorithme ftcs
    M=[]#la matrice graphique
    M.append(lavant)#ajouter la premiere ligne
    
    lapres=[0]*(p+1)
    for j in range(1,n+1):#lignes par lignes
        #condition au bord
        lapres[0]=0
        lapres[p]=0
        for i in range(1,p):#domaine vierge
            lapres[i]=A*lavant[i+1]+B*lavant[i]+A*lavant[i-1]
        M.append(lapres)
        lavant,lapres=lapres,[0]*(p+1)
    print(len(X),len(T))
    print(len(M),len(M[0]))
    
    fig = plt.figure()
    ax = fig.add_subplot(111,projection ="3d")
    Xs,Ts=np.meshgrid(X,T)
    Z=np.array(M)
    surf=ax.plot_surface(Xs,Ts,Z,rstride=1,cstride=1,cmap=plt.cm.winter,linewidth=1,antialiased=True)
    ###########################
    """Rp=np.linspace(-10,10,100)
    Rt=np.linspace(100,2000,2000)
    R,T=np.meshgrid(Rp,Rt)
    g =lambda r,t:(No/(4*mt.pi*d*t))*mt.exp(k*t-(r**2/(4*d*t)))
    c=np.vectorize(g)
    Z=c(R,T)
    surf=ax.plot_surface(R,T,Z,rstride=1,cstride=1,cmap=plt.cm.autumn,linewidth=1,antialiased=True)"""
    ###########################
    plt.title('T = '+str(ti+(j+1)*dt)+'jour'+ ' R= '+str(a)+'cm' +' k = '+str(k) + ' d = '+str(d) + ' No = '+ str(No)+' A = '+str(A))
    fig.colorbar(surf)
    plt.xlabel('Rayon',color='c')
    plt.ylabel('Temps',color='c')
    plt.show()
#finite_differnce_3d(5,10,2000,0.0012,0.0013,100,2300,200)
#mesure_stabilite(3,1000,1200,0.0012,0.0013,100,50,2,100)
finite_differnce(5,100,200,0.0012,0.0013,100,100,220)