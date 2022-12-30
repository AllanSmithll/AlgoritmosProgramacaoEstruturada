# 30/12/2022

frase = input('Digite uma frase:\n')
vezes = int(input('\nDigite um valor inteiro de vezes para repetir as vogais:\n'))

vogais = 'AaEeIiOoUuÂÃâãáÀàÁÉéÊêÍíóÓÕõôÔÚúÛú'
saida = ''

for letra in frase:
    if vogais.find(letra) >= 0:
        n = vezes    
    else:
        n = 1
    saida = saida + letra * n

print(f'\nSaída:\n{saida}')