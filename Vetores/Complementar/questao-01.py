# 30/12/2022 - Datas de quando coloquei no github

cont_par = 0
cont_impar = 0
soma = 0

n = int(input('Digite o valor de N: '))
vetor = [None]*n

for i in range(n):
  vetor[i] = int(input())
for e in vetor:
  if e % 2 == 0:
    cont_par += 1
  else:
    cont_impar += 12

for e in vetor:
  soma += e

media = soma / n

print(f'\nQuantidade de elementos pares: {cont_par}')
print(f'Quantidade de elementos ímpares: {cont_impar}')
print(f'Soma de todos os elementos: {soma}')
print(f'Média dos elementos: {media:.0f}')