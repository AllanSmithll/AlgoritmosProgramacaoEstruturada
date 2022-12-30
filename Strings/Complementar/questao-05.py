# 30/12/2022

frase = input('Forme uma frase:\n')
s = len(frase)
print('')
print('Saída:')

for i in range(s):
    print(frase[i]*(i+1))

for i in range(s-2,-1,-1):
    print(frase[i]*(i+1))