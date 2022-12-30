# 30/12/2022

# Leitura da ordem da matriz quadrada
n = int(input('Digite a ordem da matriz: '))

# Criação da matriz
m = [[None]*n for i in range(n)]

# Leitura da matriz
print('\nDigite os elementos da matriz:')
for i in range(n):
    for j in range(n):
        m[i][j] = int(input(f'm[{i}][{j}]: '))

# Exibição da matriz
print('\nMatriz:')
for i in range(n):
    for j in range(n
                   ):
        print(f'{m[i][j]:4}',end='')
    print()

# Exibição da diagonal principal
print('\nDiagonal Principal:')
for i in range(n):
    for j in range(n):
        if i == j:
            print(f'{m[i][j]:4}',end='')