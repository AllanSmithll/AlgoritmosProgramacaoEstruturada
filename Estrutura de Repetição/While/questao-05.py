resp = 'S'

while resp == 'S':

    n = int(input('Digite um número inteiro: '))

    if n % 2 == 0:
        result = 'par'
    else:
        result = 'ímpar'        

    print(f'{n} é {result}')

    resp = input('Deseja continuar (S/N)? ').upper()
    print()

print('Fim do programa')