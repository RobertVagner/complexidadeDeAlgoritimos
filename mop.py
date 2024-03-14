import numpy as np

def bubblesort(v):
    nt=0
    for i in range (1,v.shape[0]-1):
        for j in range (v.shape[0]-i):
            if v[j]>v[j+1]:
                v[j],v[j+1]=v[j+1],v[j]
                nt+=1
    return nt
 
    
def selectionSort(v):
    nt=0
    for i in range(v.shape[0]):
        n = i
        for j in range(i + 1,v.shape[0]):
            if v[j] < v[n]:
                n = j
        v[i], v[n]= v[n],v[i]
        nt+=1
    return nt
        
        
def selectionsort(v):
    nt=0
    n=v.shape[0]
    while n>1:
        m=0
        for i in range(1,n):
            if v[i]>v[m]:
                m=i
        v[n-1], v[m] = v[m],v[n-1]
        n-=1
        nt+=1
    return nt
        

def insertionSort(v):
    nt=0
    for i in range(1,v.shape[0]):
        j = i-1
        x = v[i]
        while j>=0 and x<v[j]:
            v[j+1] = v[j]
            nt+=1
            j-=1
        v[j+1]=x       
    return nt

def intercala(v,aux,p,m,u):
    aux[:]=v[:]
    i=p
    j=m+1
    for k in range(p,u+1):
        if i>m:
            v[k]= aux[j]
            j+=1
        elif j>u:
            v[k]=aux[i]
            i+=1
        elif aux [i]<aux[j]:
            v[k]=aux[i]
            i+=1
        else:
            v[k]=aux[j]
            j+=1
            
def merge(v,aux,p,u):
    if p==u:
        return
    m=(p+u)//2
    merge(v,aux,p,m)
    merge(v,aux,m+1,u)
    intercala(v,aux,p,m,u)
    
def mergesort(v):
    aux=np.empty(v.shape[0])
    merge(v,aux,0,v.shape[0]-1)
    