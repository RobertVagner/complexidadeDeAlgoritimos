
class Hashing:
    def __init__(self,np=5):
        self.m=np
        self.L=[[] for i in range(np)]
    def insere(self, chave):
        self.L[self.hash(chave)].append(chave)
    def hash(self,chave):
        soma = 0
        for i in range(len(chave)):
            soma += ord(chave[i])*(i+1)
        return soma%self.m
        
    def __repr__(self):
        return (str(self.L))
    
th = Hashing(3)

th.insere("ABC")
th.insere("CBA")