arq=open("notas_estudante.txt")

for linha in arq:
    linha = linha.rsplit()
    notas = [int (x) for x in linha[1:]]
    print (linha[0],"media = ",sum(notas)/len(notas))