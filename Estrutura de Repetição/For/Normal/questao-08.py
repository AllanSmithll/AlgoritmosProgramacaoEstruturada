import math

maior = 0

n = int(input('Digite um número inteiro: '))

for i in range(1,n+1):
    raiz = math.sqrt(i)
    if raiz == int(raiz) and i > maior:
        maior = i

print('Maior quadrado perfeito:',maior)