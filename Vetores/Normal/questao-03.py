#leitura do tamanho do vetor V
n = int(input('Digite o tamanho do vetor V: '))

#inicialização do vetor V
v = [None]*n

#leitura do vetor V
print('\nDigite os elementos do vetor A:')
for i in range(n):
    v[i] = int(input())

#leitura do valor K
k = int(input('\nDigite o valor de K: '))

#verificação se K está em V
existe = False
for e in v:
    if e == k:
        existe = True
        break

#exibição dos resultados
if existe:   # if existe == True:
    print(f'\nO valor {k} está no vetor nas seguintes posições:')
    for i in range(n):
        if v[i] == k:
            print(i)
else:
    print(f'\nO valor {k} não está no vetor')