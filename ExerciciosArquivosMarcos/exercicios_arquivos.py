arq = open('carros.txt', 'w')
# arq2 = open('carros2.txt', 'w')
# arq3 = open('carros3.txt', 'w')
# arq4 = open('carros4.txt', 'w')

#inserir
lista = []
lista.append('Uno\n')
lista.append('Gol\n')
lista.append('Up\n')
lista.append('Ka\n')
arq.writelines(lista)
arq.close()


#exercicio1
# linha = arq.readlines()
# linha.reverse()
# for i in linha:
#     arq2.writelines(str(i))
# arq2.close()


#exercicio2
# linha = arq.readlines()
# linha.sort()
# for i in linha:
#     arq3.writelines(str(i))
# arq3.close()

#exercicio3
# linha = arq.readlines()
# linha.sort()
# i = 0
# x = 1
# while i < 8:
#     linha.insert(i, f'{x} - ')
#     i = i + 2
#     x = x + 1
# for i in linha:
#     arq4.writelines(str(i))
# arq4.close()