contM = 0
contF = 0

n = int(input('Quantidade de pessoas: '))

for i in range(n):

    sexo = input('\nSexo(M/F): ').upper()

    if sexo == 'M':
        contM = contM + 1
    else:
        contF = contF + 1

    percM = contM / n * 100
    percF = contF / n * 100

    print(f'Percentual de homens: {percM:.0f}%')
    print(f'Percentual de muheres: {percF:.0f}%')