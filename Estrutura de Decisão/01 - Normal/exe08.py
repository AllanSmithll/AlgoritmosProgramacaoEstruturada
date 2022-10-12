# Calculadora básica em Python

x = int(input('1º operando: '))
y = int(input('2º operando: '))
op = input('Operador: ')

print('\nResultado: ',end='')
if op == '+':
  print(x + y)
elif op == '-':
  print(x - y)
elif op == 'x' or op == '*':
  print(x * y)
elif op == '/':
  print(x / y)
elif op == '%':
  print(x % y)
else:
  print('Operador desconhecido')