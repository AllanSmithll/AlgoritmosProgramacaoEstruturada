# 30/12/2022

n = 6
cont = 0
numeros = [None]*n

print(f'Digite {n} números distintos')

for i in range(n):

    while True:
        
        x = int(input())

        existe = False
        for j in range(i):
            if x == numeros[j]:
                existe = True
                break
        if existe:
            print('Número já existente. Digite novamente')
            continue

        numeros[i] = x
        cont += 1
        break

print(f'\nNúmeros válidos: {numeros}')