# 30/12/2022

ordem = int(input('Digite a ordem da matriz quadrada: '))

m = [[None]*ordem for i in range(ordem)]

print('\nDigite os elementos da matriz:')
for i in range(ordem):
  for j in range(ordem):
    m[i][j] = int(input(f'm[{i}][{j}]:'))

print('\nMatriz:')
for i in range(ordem):
  for j in range(ordem):
    print(f'{m[i][j]:4}', end='')
  print()

  quadradoM = True

diagP = 0
for i in range(ordem):
    diagP += m[i][j]

diagS = 0
for i in range(ordem):
      diagS += m[ordem-i-1][i]
if diagS != diagP:
    quadradoM = False

for i in range(ordem):
    somaL = 0
    for j in range(ordem):
        somaL += m[i][j]
    if somaL != diagP:
        quadradoM = False

for j in range(ordem):
    somaC = 0
    for i in range(ordem):
        somaC += m[i][j]
    if somaC != diagP:
        quadradoM = False

if quadradoM:
    print('\nÉ quadrado mágico')
else:
    print('\nNão é quadrado mágico')