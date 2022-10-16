flag = 999
soma = 0
cont = 0

print(f'Digite vários números (para encerrar, digite {flag})')
num = int(input())

while num != flag:
    soma = soma + num
    cont = cont + 1
    num = int(input())

media = soma / cont

print(f'Média = {media:.1f}')