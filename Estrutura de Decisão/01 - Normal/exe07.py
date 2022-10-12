# Cálculo de IMC

Massa = float(input('Quantos quilos? '))
Alt = float(input('Altura? '))
#Altura#
Imc = Massa / (Alt ** 2)

if Alt < 26:
   ind = 'Normal'
#Índice#
elif Alt < 30:
   ind = 'Obeso'
else:
   ind = 'Obeso Mórbido'

print(f'Seu IMC {Imc:.2f} possui grau de obesidade {ind}.')
(' ')
print('11/04/2022')