# 30/12/2022

ordem = int(input('Ordem da matriz: '))

m  = [[None]*ordem for i in range(ordem)]

print('\nDigite números de 0 a 1 para a matriz: ')

for i in range(ordem):
  for j in range(ordem):
    m[i][j] = int(input(f'm[{i}][{j}]: '))

print('\nMatriz')
for i in range(ordem):
    for j in range(ordem):
        print(f'{m[i][j]:4}',end='')
    print()

test_lin = True
for i in range (ordem):
  cont = 0
  for j in range(ordem):
      if m[i][j] == 1:
        cont += 1
  if cont != 1:
      test_lin = False
      break
    
test_col = True
for i in range(ordem):
  cont = 0
  for j in range(ordem):
     if m[i][j] == 1:
       cont += 1
  if cont != 1:
    test_col = False
    break

if test_lin and test_col:
  print('\nÉ uma matriz de permutação.')
else:
  print('\nNão é uma matriz de permutação.')