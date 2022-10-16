#testando com 5 ao invés de 30
n = 5  

#inicialização do vetor V
v = [None]*n

#leitura do vetor V
print('Digite os elementos do vetor A:')
for i in range(n):
    v[i] = int(input())

#leitura do valor K
k = int(input('Digite o valor de K: '))

#contagem das ocorrências
cont = 0
for e in v:
    if e == k:
        cont += 1

#exibição do resultado
print(f'\nNº de ocorrências: {cont}')