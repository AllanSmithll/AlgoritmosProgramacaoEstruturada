# 30/12/2022

#leitura do valor de N
n = int(input('Digite o valor de N: '))

#inicialização dos vetores A, B e C
a = [None]*n
b = [None]*n
c = [None]*(n*2)

#leitura do vetor A
print('\nDigite os elementos do vetor A:')
for i in range(n):
    a[i] = int(input('A['+str(i)+']: '))

#leitura do vetor B
print('\nDigite os elementos do vetor B:')
for i in range(n):
    b[i] = int(input('B['+str(i)+']: '))

#geração do vetor C
for i in range(n):
    c[i*2] = a[i]
    c[i*2+1] = b[i]

#impressão dos vetores A, B e C
print()
print('A = ',a)
print('B = ',b)
print('C = ',c)