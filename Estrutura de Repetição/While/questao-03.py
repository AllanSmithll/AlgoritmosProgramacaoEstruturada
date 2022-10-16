flag = 0

print(f'Digite vários números (para encerrar, digite {flag})')
num = int(input())

maior = num
menor = num

while num != flag:

    if num > maior:
        maior = num

    if num < menor:
        menor = num

    num = int(input())

print(f'Maior = {maior}')
print(f'Menor = {menor}')