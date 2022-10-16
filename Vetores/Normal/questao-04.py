# inicialização das variáveis
n = 10
numeros = [None]*n

# leitura dos números 
for i in range(n):
    numeros[i] = int(input(f'numero[{i}]: '))

# exibição dos números que estão nos índices pares
print('\nNúmeros que estão nos índices pares:')
for i in range(0,n,2):
    print(numeros[i])

# exibição dos números que estão nos índices ímpares
print('\nNúmeros que estão nos índices ímpares:')
for i in range(1,n,2):
    print(numeros[i])