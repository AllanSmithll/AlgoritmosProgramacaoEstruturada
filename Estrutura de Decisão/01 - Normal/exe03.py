# Maior número entre os três digitados

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o último número: '))

if num1 > num2 and num1 > num3:
  result = num1
elif num2 > num1 and num2 > num3:       
  result = num2
elif num3 > num1 and num3 > num2:
  result = num3

print(f'{result} é o maior.')