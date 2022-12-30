# 30/12/2022

ordem = 3

m = [[None]*ordem for i in range(ordem)]

import random
for i in range(ordem):
    for j in range(ordem):
        m[i][j] = random.randint(1,10)

print('\nMatriz:')
for i in range(ordem):
    for j in range(ordem):
        print(f'{m[i][j]:4}',end='')
    print()

print('\nSoma de cada linha:')
for i in range(ordem):
    s = 0
    for j in range(ordem):
        s += m[i][j]
    print(f'{s:4}')

print('\nSoma de cada coluna:')
for j in range(ordem):
    s = 0
    for i in range(ordem):
        s += m[i][j]
    print(f'{s:4}',end='')

print('\n\nSoma da diagonal principal:')
s = 0
for i in range(ordem):
    for j in range(ordem):
        if i == j:
            s += m[i][j]
print(f'{s:4}')

print('\nSoma da diagonal secundária:')
s = 0
for i in range(ordem):
    for j in range(ordem):
        if i == ordem-j-1:
            s += m[i][j]
print(f'{s:4}')

print('\nSoma de toda a matriz:')
s = 0
for i in range(ordem):
    for j in range(ordem):
        s += m[i][j]
print(f'{s:4}')