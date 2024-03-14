
L=[]

L.append('Uno\n')
L.append('Gol\n')
L.append('Up\n')
L.append('Ka\n')

arq=open('carros4.txt','w')
L.sort()

for i in range(len(L)):
    arq.write(str(i+1)+' - '+L[i])

arq.close()