qtd = 5 #vamos testar o programa com poucos números, para agilizar a execução. 

print(f'Digite {qtd} números inteiros:')

for i in range(qtd):

    num = int(input())

    if i == 0: #testa se é a 1ª iteração do for
        maior = num
    else:
        if num > maior:
            maior = num

print(f'Maior = {maior}')