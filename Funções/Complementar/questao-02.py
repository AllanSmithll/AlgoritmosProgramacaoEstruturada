# 30/12/2022

def primo(n):
    '''Função que diz se o número é primo'''
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
           return False
    return True

#Programa principal
print('Números primos entre 1 e 100:')
for i in range(1, 101):
    if primo(i):
       print(i, end=' ')