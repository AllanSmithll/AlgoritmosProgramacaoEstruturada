# 30/12/2022

#leitura do tamanho do vetor
n = int(input('Digite o tamanho do vetor: '))

#inicialização do vetor
v = [None]*n

#leitura dos elementos do vetor
print(f'Digite os {n} elementos do vetor:')
for i in range(n):
    v[i] = int(input())

#exibição do vetor antes da inversão
print(f'\nAntes da inversão: {v}')

#inversão da ordem dos elementos do vetor
j = n-1
for i in range(n//2):
    aux = v[i]
    v[i] = v[j]
    v[j] = aux
    j = j-1

#exibição do vetor depois da inversão
print(f'\nDepois da inversão: {v}')