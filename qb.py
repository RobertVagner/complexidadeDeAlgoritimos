
arq=open("qb.txt")

linhas = arq.readlines()

for linha in linhas:
    linha = linha.rsplit()
    print (linha[0],linha[1],"obteve a avaliação ",linha[-1])