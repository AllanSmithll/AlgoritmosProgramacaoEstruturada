# 30/12/2022

def vertical(s):
    '''Imprime uma frase de forma verticalizada'''
    for letra in s:
        print(letra)

frase = input('Forme uma frase: ')
print('\nDe forma verticalizada:')
vertical(frase)