import sys

soma = 0
for num in sys.argv[1:]:
    soma+=int(num)
    
print (soma)