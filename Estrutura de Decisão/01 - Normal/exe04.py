# Pronome de tratamento

name = input('Escreva seu nome: ')
sex = input('Sexo (M ou F): ')
sex = sex.upper()

if sex == 'M':
  trat = 'Sr'
else:
  trat = 'Sra'
  
print(f'Olá, {trat}. {name}!')
print(' ')
print('Feito em 07/04/2022')