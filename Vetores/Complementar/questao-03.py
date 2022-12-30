# 30/12/2022

n = 6
numeros = [None]*n

for i in range(n):
    numeros[i] = int(input(str(i+1) + 'º número: '))

print()

for i in range(n):
    
    existe = False
    for j in range(n):
        if numeros[i] == numeros[j] and i != j:
            existe = True
            break
    
    if existe:
        print(numeros[i],'repete')
    else:
        print(numeros[i],'não repete')