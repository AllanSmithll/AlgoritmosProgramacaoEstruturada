# 30/11/2022 - Data que adicionei

nlin = 2  # número de linhas da matriz
ncol = 3  # número de colunas da matriz

# Criação das matrizes
a = [[None]*ncol for i in range(nlin)]
b = [[None]*ncol for i in range(nlin)]
c = [[None]*ncol for i in range(nlin)]

# Leitura da matriz A
print('Digite os elementos da Matriz A:')
for i in range(nlin):
    for j in range(ncol):
        a[i][j] = int(input(f'A[{i}][{j}]: '))

# Leitura da matriz B
print('\nDigite os elementos da Matriz B:')
for i in range(nlin):
    for j in range(ncol):
        b[i][j] = int(input(f'B[{i}][{j}]: '))

# Cálculo da matriz C
for i in range(nlin):
    for j in range(ncol):
        c[i][j] = a[i][j] + b[i][j]

# Impressão da matriz A
print('\nMatriz A:')
for i in range(nlin):
    for j in range(ncol):
        print(f'{a[i][j]:4}',end='')
    print()
      
# Impressão da matriz B
print('\nMatriz B:')
for i in range(nlin):
    for j in range(ncol):
        print(f'{b[i][j]:4}',end='')
    print()

# Impressão da matriz C
print('\nMatriz C:')
for i in range(nlin):
    for j in range(ncol):
        print(f'{c[i][j]:4}',end='')
    print()