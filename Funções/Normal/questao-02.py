# 30/12/2022

def fatorial(n):
    '''Fatorial de n!'''
    if n < 0:
        return None
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

#Fatorial
valor = int(input('Cálculo do valor em fatorial: '))
result = fatorial(valor)
print('\n{valor}! =', result)