# 30/12/2022

def soma(vetor):
    '''Soma entre todos os números de uma lista'''
    somador = 0
    for i in range(len(vetor)):
        somador += vetor[i]
    return somador

v = [6, 3, 8, 7, 2, 5]
s = soma(v)
print(f'\nA soma de todos os elementos do vetor é igual a {s}.')