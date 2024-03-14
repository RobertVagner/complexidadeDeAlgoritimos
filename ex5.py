ocorrencia = 0
codon = input("Entre com o códon: ")
arq = open("seq.txt","r")
texto = arq.read();
textp = texto.replace('\n', '')
print(f"Total de ocorrências: {texto.count(codon)}" )
input()