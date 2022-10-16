n = int(input('Informe o valor de N: '))
x = int(input('Informe o valor de X: '))
y = int(input('Informe o valor de Y: '))

print('\nOs múltiplos de',n,'entre',x,'e',y,'são:')

for i in range(x,y+1):
    if i % n == 0:
        print(i,end=' ')