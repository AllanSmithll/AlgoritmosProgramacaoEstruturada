# 30/12/2022

import random

#leitura da ordem das matrizes
ord = int(input('Ordem da matriz quadrada: '))

#inicialização das variáveis
A = [[None]*ord for i in range(ord)]
B = [[None]*ord for i in range(ord)]

#geração aleatória da matriz A
for lin in range(ord):
    for col in range(ord):
        A[lin][col] = random.randint(1,20)

#geração da matriz B
for lin in range(ord):
    for col in range(ord):
        if lin == col or lin + col == ord - 1:
            B[lin][col] = 0
        else:
            B[lin][col] = A[lin][col] + lin + col

#impressão da matriz A
print('\nMatriz A')
for lin in range(ord):
    for col in range(ord):
        print(f'{A[lin][col]:3}',end='')
    print()

#impressão da matriz B
print('\nMatriz B')
for lin in range(ord):
    for col in range(ord):
        print(f'{B[lin][col]:3}',end='')
    print()