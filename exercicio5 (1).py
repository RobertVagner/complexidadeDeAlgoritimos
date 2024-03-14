arquivo = open("seq.txt")
sequencia= input("digite a sequencia: ")
contador=0
for linha in arquivo:
  contador+=int(linha.count(sequencia))
print("Total De Ocorrências: ",contador)