n = int(input('Digite o tamanho do vetor A: '))

a = [None]*n
b = [None]*n

print('Digite os elementos do vetor A:')
for i in range(n):
    a[i] = int(input(f'A[{i}]: '))

k = int(input('Digite o valor de K: '))

for i in range(n):
    b[i] = a[i] * k

print()
print('A =',a)
print('K =',k)
print('B =',b)