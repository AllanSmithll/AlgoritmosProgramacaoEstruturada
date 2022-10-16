a = 0
b = 1
n = int(input('Digite o número de termos desejados: '))

print('Sequência de Fibonacci:',a,b,end=' ')

for i in range(3, n+1):
  c = a + b
  print(c, end=' ')
  a = b
  b = c
  