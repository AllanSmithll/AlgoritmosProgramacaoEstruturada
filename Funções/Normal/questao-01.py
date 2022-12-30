# 30/12/2022 -> Data de push pro Github

def menor(num1, num2, num3):
    '''Função que determina o menor valor'''
    if num1 < num2 and num1 < num3:
        return num1
    elif num2 < num1 and num2 < num3:
        return num2
    elif num3 < num1 and num3 < num2:
        return num3

#Dar 3 valores para a função
print('\nInformar 3 valores:')
n1 = str(input('Primeiro valor: '))
n2 = str(input('Segundo valor: '))
n3 = str(input('Terceiro valor: '))
m = menor(n1, n2, n3)
print(f'O menor valor entre eles é {m}.')