import matplotlib.pyplot as plt
import math as mt
import numpy as np
from mpl_toolkits import mplot3d
import random as rd
def count_2(M,n):
    res=0
    center=int((len(M)+1)/2)-1
    for i in range(center-n,center+n+1):
        for j in range(center-n,center+n+1):
            if M[i][j]==1:
                res+=1
    return res
def count_1(M):
    res=0
    n=len(M)
    for i in range(n):
        for j in range(n):
            if M[i][j]==1:
                res+=1
    return res
def pick(T):
    n=len(T)
    return T[rd.randint(0,n-1)]
def visualise(T):
    l=len(T)
    plt.hlines(y=np.arange(0, l)+0.5, xmin=np.full(l, 0)-0.5, xmax=np.full(l, l)-0.5, color="white")
    plt.vlines(x=np.arange(0, l)+0.5, ymin=np.full(l, 0)-0.5, ymax=np.full(l, l)-0.5, color="white")
    #cmap = plt.cm.winter
    #plt.imshow(T,cmap=cmap)
    plt.imshow(T)
    plt.show()
def creer_matrix_zero(n):
    T=np.zeros((n,n))
    return T
def creer_matrix_hexa1(n):#n:impaire
    T=creer_matrix_zero(n)
    center=int((n+1)/2)-1
    #print('center',center)
    T[center][center],T[center-1][center],T[center][center+1],T[center+1][center+1],T[center+1][center],T[center+1][center-1],T[center][center-1]=1,1,1,1,1,1,1
    return T
def creer_matrix_hexa0(n):#n:impaire
    T=creer_matrix_zero(n)
    center=int((n+1)/2)-1
    T[center][center]=1
    return T
def distance(a,b,c,d):
    return mt.sqrt((a-c)**2 + (b-d)**2)
def inertie_app(i,j,m,n,c):
    return distance(m,n,c,c)>=distance(i,j,c,c)
def voisin(T,i,j):
    n=len(T)
    center=int((n+1)/2)-1
    voisin_contact=[]#passer avec proba p , en contact
    voisin_nocontact=[]#passer avec proba 1-p,sans contact
    if T[i][j]==1:
        if T[i-1][j]==T[i][j+1]==T[i+1][j+1]==T[i+1][j]==T[i+1][j-1]==T[i][j-1]==1:#tourner ne peut pas migrer
            return [],[]
        else:
            if T[i-1][j]==0 and inertie_app(i,j,i-1,j,center)==True:#1
                if T[i][j+1]==0 and T[i][j-1]==0:
                    voisin_nocontact.append((i-1,j))
                else: voisin_contact.append((i-1,j))
            if T[i][j+1]==0 and inertie_app(i,j,i,j+1,center)==True:#2
                if T[i-1][j]==0 and T[i+1][j+1]==0:
                    voisin_nocontact.append((i,j+1))
                else: voisin_contact.append((i,j+1))
            if T[i+1][j+1]==0 and inertie_app(i,j,i+1,j+1,center)==True:#3
                if T[i][j+1]==0 and T[i+1][j]==0:
                    voisin_nocontact.append((i+1,j+1))
                else: voisin_contact.append((i+1,j+1))
            if T[i+1][j]==0 and inertie_app(i,j,i+1,j,center)==True:#4
                if T[i+1][j+1]==0 and T[i+1][j-1]==0:
                    voisin_nocontact.append((i+1,j))
                else: voisin_contact.append((i+1,j))
            if T[i+1][j-1]==0 and inertie_app(i,j,i+1,j-1,center)==True:#5
                if T[i+1][j]==0 and T[i][j-1]==0:
                    voisin_nocontact.append((i+1,j-1))
                else: voisin_contact.append((i+1,j-1))
            if T[i][j-1]==0 and inertie_app(i,j,i,j-1,center)==True:#6
                if T[i-1][j]==0 and T[i+1][j-1]==0:
                    voisin_nocontact.append((i,j-1))
                else: voisin_contact.append((i,j-1))
            return voisin_contact,voisin_nocontact
    else: return [],[]#n'est pas qualifiée
def migration_animation(n,frame,p):#n taille de la matrice , frame le temps , p proba
    desher=[]
    T=creer_matrix_hexa1(n)
    M_apres=creer_matrix_zero(n)
    ###
    l=len(T)
    #plt.hlines(y=np.arange(0, l)+0.5, xmin=np.full(l, 0)-0.5, xmax=np.full(l, l)-0.5, color="white")
    #plt.vlines(x=np.arange(0, l)+0.5, ymin=np.full(l, 0)-0.5, ymax=np.full(l, l)-0.5, color="white")
    plt.imshow(T)
    plt.title('t= '+str(0))
    ###
    for k in range(1,frame+1):
        for i in range(1,n-1):
            for j in range(1,n-1):
                if T[i][j]==1 :
                    desher.append((i,j))
                    voisin_contact,voisin_nocontcat=voisin(T,i,j)[0],voisin(T,i,j)[1]
                    if voisin_contact !=[] and voisin_nocontcat==[]:##probleme wch is vide
                        for element in voisin_contact:
                            M_apres[element[0]][element[1]]=1
                    if voisin_nocontcat !=[] and voisin_contact==[]:##probleme wch is vide
                        for element in voisin_nocontcat:
                            M_apres[element[0]][element[1]]=1

                    if voisin_contact !=[] and voisin_nocontcat !=[]:##probleme wch is vide
                        prob=rd.uniform(0,1)                    
                        if prob<=p:#zone de contact
                            for element in voisin_contact:
                                M_apres[element[0]][element[1]]=1
                        else:
                            for element in voisin_nocontcat:
                                M_apres[element[0]][element[1]]=1
                        
        center=int((n+1)/2)-1
        for e in desher:
            M_apres[e[0]][e[1]]=0
        M_apres[center][center],M_apres[center-1][center],M_apres[center][center+1],M_apres[center+1][center+1],M_apres[center+1][center],M_apres[center+1][center-1],M_apres[center][center-1]=1,1,1,1,1,1,1
        
        ###visiualise
        plt.pause(0.001)
        l=len(M_apres)
        #plt.hlines(y=np.arange(0, l)+0.5, xmin=np.full(l, 0)-0.5, xmax=np.full(l, l)-0.5, color="white")
        #plt.vlines(x=np.arange(0, l)+0.5, ymin=np.full(l, 0)-0.5, ymax=np.full(l, l)-0.5, color="white")
        plt.imshow(M_apres)
        plt.title('t= '+str(k)+' proba= '+ str(p))
        ###
        T,M_apres=M_apres,creer_matrix_zero(n)
        desher=[]
    plt.show()
def migration(n,frame,p):#n taille de la matrice , frame le temps , p proba
    desher=[]
    T=creer_matrix_hexa1(n)
    M_apres=creer_matrix_zero(n)
    ###
    l=len(T)
    #plt.hlines(y=np.arange(0, l)+0.5, xmin=np.full(l, 0)-0.5, xmax=np.full(l, l)-0.5, color="white")
    #plt.vlines(x=np.arange(0, l)+0.5, ymin=np.full(l, 0)-0.5, ymax=np.full(l, l)-0.5, color="white")
    #plt.imshow(T)
    #plt.title('t= '+str(0))
    ###
    for k in range(1,frame+1):
        for i in range(1,n-1):
            for j in range(1,n-1):
                if T[i][j]==1:
                    voisin_contact,voisin_nocontcat=voisin(T,i,j)[0],voisin(T,i,j)[1]
                    if voisin_contact !=[] and voisin_nocontcat==[]:##probleme wch is vide
                        for element in voisin_contact:
                            M_apres[element[0]][element[1]]=1
                    if voisin_nocontcat !=[] and voisin_contact==[]:##probleme wch is vide
                        for element in voisin_nocontcat:
                            M_apres[element[0]][element[1]]=1

                    if voisin_contact !=[] and voisin_nocontcat !=[]:##probleme wch is vide
                        prob=rd.uniform(0,1)                    
                        if prob<=p:#zone de contact
                            for element in voisin_contact:
                                M_apres[element[0]][element[1]]=1
                        else:
                            for element in voisin_nocontcat:
                                M_apres[element[0]][element[1]]=1
                        
        center=int((n+1)/2)-1
        for e in desher:
            M_apres[e[0]][e[1]]=0
        M_apres[center][center],M_apres[center-1][center],M_apres[center][center+1],M_apres[center+1][center+1],M_apres[center+1][center],M_apres[center+1][center-1],M_apres[center][center-1]=1,1,1,1,1,1,1
        
        ###visiualise
        #plt.pause(0.001)
        l=len(M_apres)
        #plt.hlines(y=np.arange(0, l)+0.5, xmin=np.full(l, 0)-0.5, xmax=np.full(l, l)-0.5, color="white")
        #plt.vlines(x=np.arange(0, l)+0.5, ymin=np.full(l, 0)-0.5, ymax=np.full(l, l)-0.5, color="white")
        
        ###
        T,M_apres=M_apres,creer_matrix_zero(n)
        desher=[]
    #plt.imshow(T)
    #plt.title('t= '+str(k)+' proba= '+ str(p))
    #plt.show()
    return T
def count_cell(n,frame,p):
    desher=[]
    T=creer_matrix_hexa1(n)
    M_apres=creer_matrix_zero(n)
    cell=[count_1(T)]
    fr=[0]
    for k in range(1,frame+1):
        for i in range(1,n-1):
            for j in range(1,n-1):
                if T[i][j]==1:
                    voisin_contact,voisin_nocontcat=voisin(T,i,j)[0],voisin(T,i,j)[1]
                    if voisin_contact !=[] and voisin_nocontcat==[]:##probleme wch is vide
                        for element in voisin_contact:
                            M_apres[element[0]][element[1]]=1
                    if voisin_nocontcat !=[] and voisin_contact==[]:##probleme wch is vide
                        for element in voisin_nocontcat:
                            M_apres[element[0]][element[1]]=1

                    if voisin_contact !=[] and voisin_nocontcat !=[]:##probleme wch is vide
                        prob=rd.uniform(0,1)                    
                        if prob<=p:#zone de contact
                            for element in voisin_contact:
                                M_apres[element[0]][element[1]]=1
                        else:
                            for element in voisin_nocontcat:
                                M_apres[element[0]][element[1]]=1
        center=int((n+1)/2)-1
        for e in desher:
            M_apres[e[0]][e[1]]=0
        M_apres[center][center],M_apres[center-1][center],M_apres[center][center+1],M_apres[center+1][center+1],M_apres[center+1][center],M_apres[center+1][center-1],M_apres[center][center-1]=1,1,1,1,1,1,1
        T,M_apres=M_apres,creer_matrix_zero(n)
        cell.append(count_1(T))
        fr.append(k)
        desher=[]
    plt.subplot(1,2,1)
    plt.title('iteration '+str(frame) + ' p='+str(p))
    plt.imshow(T)
    l=len(T)
    #plt.hlines(y=np.arange(0, l)+0.5, xmin=np.full(l, 0)-0.5, xmax=np.full(l, l)-0.5, color="Black")
    #plt.vlines(x=np.arange(0, l)+0.5, ymin=np.full(l, 0)-0.5, ymax=np.full(l, l)-0.5, color="Black")
    plt.subplot(1,2,2)
    plt.style.use('seaborn')
    plt.xlabel('iteration')
    plt.ylabel('#cellules')
    plt.plot(fr,cell)
    plt.pause(0.001)
    plt.show()
def concentration(n,frame,p):####meezll khassha lmkma
    plt.style.use('seaborn')
    T=migration(n,frame,p)
    Rayon=[]
    concentration=[]
    for k in range(1,int((len(T)+1)/2)-5):
        Rayon.append(k*35)
        #Rayon.append(k)
        concentration.append(count_2(T,k)/((2*(35*k))**2))
    plt.plot(Rayon,concentration,label='p= '+str(p))

    return concentration,Rayon
    '''
    plt.title('iteration '+ str(frame))
    plt.xlabel('rayon en um')
    plt.ylabel('cellules/(um)**2')
    plt.legend()
    plt.show()'''
def concentration_lot(n,frame,p):####meezll khassha lmkma lot of p=[]
    plt.style.use('seaborn')
    for proba in p:
        T=migration(n,frame,proba)
        Rayon=[]
        concentration=[]
        for k in range(1,int((len(T)+1)/2)-5):
            Rayon.append(k*35)
            concentration.append(count_2(T,k)/((2*(35*k))**2))
        plt.plot(Rayon,concentration,label='p= '+str(proba))
        Rayon=[]
        concentration=[]
    plt.title('iteration '+ str(frame))
    plt.xlabel('rayon en um')
    plt.ylabel('cellules/(um)**2')
    plt.legend()
    plt.show()
def concentration_3d(n,frame,p):
    plt.style.use('seaborn')
    fig = plt.figure()
    ax = fig.add_subplot(111,projection ="3d")
    time=[]
    Rayon=[]
    Matrice=[]
    for i in range(0,frame):
        time.append(i)
        c=concentration(n,i,p)
        Matrice.append(c[0])
        Rayon=c[1]
    Rx,Ts=np.meshgrid(Rayon,time)
    plt.xlabel('Rayon en um')
    plt.ylabel('iteration')
    Z=np.array(Matrice)
    plt.title('concentration tumorale en cellules/(um)**2')
    surf=ax.plot_surface(Rx,Ts,Z,rstride=1,cstride=1,cmap=plt.cm.winter,linewidth=1,antialiased=True)
    fig.colorbar(surf)
    plt.show()
#migration_animation(100,30,0.5)
#migration(50,100,0.5)
concentration_3d(200,100,0.5)
#count_cell(52,2,0.5)