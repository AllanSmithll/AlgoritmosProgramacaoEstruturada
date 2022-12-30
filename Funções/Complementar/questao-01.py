# 30/12/2022 - Última pasta publicada no GitHub

def vogal(letra):
    '''Função que manda as vogais não acentuadas'''
    return letra in "AaEeIiOoUu"

#Tem VOGAL?
cont = 0
frase = input('Forme uma frase (sem acento): ')
for i in frase:
  if vogal(i):
    cont += 1
print(f'A frase tem {cont} vogais.')