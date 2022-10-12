# Conceito de um estudante universitário

nome = input('Nome: ')
conc = input('Conceito: ').upper()

if conc == 'A':
    rec = 'Fortemente recomendado'
elif conc == 'B' or conc == 'C':
    rec = 'Recomendado'
else:
    rec = 'Não recomendado'

print(f'O estudante {nome} é {rec}.')
(' ')
print('11/04/2022')