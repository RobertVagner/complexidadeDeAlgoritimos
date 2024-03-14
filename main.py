from mop import *
import numpy as np
import time

A = np.random.randint(1,100,3000)
B=A.copy()
C=A.copy()
D=A.copy()
#print("Vetor desordenado...........:",A)

ti = time.time()
nt=bubblesort(A)
tf=time.time()
print("Vetor ordenado bubblesort...:",tf-ti,nt)

ti = time.time()
nt=selectionsort(B)
tf=time.time()
print("Vetor ordenado selectionsort:",tf-ti,nt)

ti = time.time()
nt=insertionSort(C)
tf=time.time()
print("Vetor ordenado insertionSort:",tf-ti,nt)

ti=time.time()
mergesort(D)
tf=time.time()

print ("Merge Sort: ",tf-ti)