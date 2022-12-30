# 30/12/2022

def lerMat(nl,nc):
    '''Função para gerar e ler uma matriz'''
    m = [[None]*nc for i in range(nl)]
    for i in range(nl):
        for j in range(nc):
            m[i][j] = int(input())
    return m

def somaMat(a,b):
    '''Função para somar duas matrizes'''
    nl = len(a)
    nc = len(a[0])
    c = [[None]*nc for i in range(nl)]
    for i in range(nl):
        for j in range(nc):
            c[i][j] = a[i][j] + b[i][j]
    return c

def impMat(m):
    '''Função para imprimir uma matriz'''
    nl = len(m)
    nc = len(m[0])
    for i in range(nl):
        for j in range(nc):
            print(f'{m[i][j]:4}',end='')
        print()


#Programa principal
# Leitura da ordem das matrizes
print('Informe a ordem da matriz:')
nlin = int(input('Nº de linhas: '))
ncol = int(input('Nº de colunas: '))

# Leitura da 1ª matriz
print('\nDigite os elementos da 1ª matriz:')
m1 = lerMat(nlin,ncol)

# Leitura da 2ª matriz
print('\nDigite os elementos da 2ª matriz:')
m2 = lerMat(nlin,ncol)

# Cálculo da matriz soma
ms = somaMat(m1,m2)

# Impressão da 1ª matriz
print('\n1ª Matriz:')
impMat(m1)     

# Impressão da 2ª matriz
print('\n2ª Matriz:')
impMat(m2)

# Impressão da matriz soma
print('\nMatriz Soma:')
impMat(ms)