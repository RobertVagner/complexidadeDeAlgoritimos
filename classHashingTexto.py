
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
    
    def pertence(self,chave):
        return chave in self.L[self.hash(chave)] 
    
    def remove(self,chave):
        if self.pertence(chave):
            self.L[self.hash(chave)].remove(chave)
            return True
        else:
            return False
        
    def hashtxt(nomearq):
        arq = open(nomearq)
        for linha in arq:
            for palavra in linha.rsplit():
                for letra in palavra:
                    print(hex(ord(letra)%16)[2],end='')
    
th = Hashing(3)

th.insere("Ana")
th.insere("Bia")
th.insere("Eva")
th.insere("Gil")
th.insere("Ivo")
th.insere("Leo")
th.insere("Rui")