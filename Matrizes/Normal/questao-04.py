# 30/12/2022

y = 3  
x = 2

# Criação das matrizes
c = [[None]*y for i in range(x)]
t = [[None]*x for i in range(y)]

# Leitura da matriz N
print('Digite os elementos da Matriz C:')
for i in range(x):
    for j in range(y):
        c[i][j] = int(input(f'C[{i}][{j}]: '))

# Geração da matriz T (transposta)
for i in range(x):
    for j in range(y):
        t[j][i] = c[i][j]

# Impressão da matriz C
print('\nMatriz C:')
for i in range(x):
    for j in range(y):
        print(f'{c[i][j]:4}',end='')
    print()
      
# Impressão da matriz T
print('\nMatriz Ct (transposta):')
for i in range(y):
    for j in range(x):
        print(f'{t[i][j]:4}',end='')
    print()