ns = int(input("Entre com um numero: "))

for i in range(1, ns + 1):
    c = 1
    while True:
        print(c, end=' ')
        if c == i:
            break
        c +=1
    print()