# 30/12/2022

ri = 30
rf = 38
ai = 1
af = 10
nlin = af - ai + 1
ncol = rf - ri + 1
mat = [[0]*ncol for i in range(nlin)]
flag = 0

print('Informe o local de cada acidente')
print('Para encerrar, digite 0 para a Av.')
while True:
    print()
    av = int(input(f'Av. ({ai} a {af}): '))
    if av == flag:
        break
    rua = int(input(f'Rua ({ri} a {rf}): '))
    lin = av - ai
    col = rua - ri 
    mat[lin][col] += 1

print('\nMAPA DOS ACIDENTES')
print('\nRua/Av.',end='')
for i in range(ncol):
    print(f'{i+ri:4}',end='')
print()

#exibição da matriz de acidentes
for i in range(nlin):
    print(f'{i+ai:4}   ',end='')
    for j in range(ncol):
        if mat[i][j] == 0:
            valor = '-'
        else:
            valor = mat[i][j]
        print(f'{valor:>4}',end='')
    print('')