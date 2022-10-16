flag = 'X'
total_geral = 0

print(f'Informe o código e a quantidade dos itens.\nPara encerrar, digite o código "{flag}"')
cod = input('\nCódigo: ').upper()

while cod != flag:

    quant = int(input('Quantidade: '))
    
    if cod == 'H':
        preco = 5.00
    elif cod == 'C':
        preco = 6.00
    elif cod == 'B':
        preco = 7.00
    else:
        preco = 4.00
    
    total_item = preco * quant
    total_geral = total_geral + total_item
    
    cod = input('\nCódigo: ').upper()

print(f'\nTotal a pagar: R$ {total_geral:.2f}')