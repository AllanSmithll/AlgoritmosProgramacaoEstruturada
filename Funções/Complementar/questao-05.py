# 30/12/2022

def fat(n):
    '''Função para calcular o fatorial'''
    f = 1
    for i in range(1,n+1):
        f *= i
    return f

def pot(x, y):
    '''Função para calcular a potência'''
    return x ** y


#Programa principal
x = float(input('Entre com o valor de x: '))

n = 0
s = 0
for i in range(1,21):
    t = pot(x,n) / fat(n)
    if i % 2 == 1:
        s += t
    else:
        s -= t
    n += 2

print()
print('Meu resultado:',s)

import math
print('Função cos   :',math.cos(x))