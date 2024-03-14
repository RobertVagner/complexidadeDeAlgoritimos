n = int(input("Entre com a quantidade de números: "))
L = []
for i in range(n):
    L.append(int(input(f"Entre com {i + 1}º número: "))) 
L.sort()
print(L)
input()