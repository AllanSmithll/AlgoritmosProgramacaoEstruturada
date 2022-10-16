f = 1

n = int(input('Entre com um número inteiro: '))

for i in range(2,n+1):
    f = f * i

print(f'{n}! = {f}')