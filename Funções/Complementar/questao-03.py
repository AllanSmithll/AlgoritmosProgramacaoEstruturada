# 30/12/2022

def leitura(v):
    '''Função para ler um vetor'''
    for i in range(len(v)):
        v[i] = int(input())  

def media(v):
    '''Função para calcular a média de um vetor'''
    soma = 0
    for i in range(len(v)):
        soma += v[i]
    return soma/len(v)

def contagem(v,n):
    '''Função para contar os elementos abaixo da média'''
    cont = 0
    for i in range(len(v)):
        if v[i] < n:
            cont += 1
    return cont

#Programa principal
qtd = 20  #Testando com apenas 5 elementos
x = [None]*qtd
print(f'Digite {qtd} números inteiros:')
leitura(x)
m = media(x)
c = contagem(x,m)
print(f'A média do elementos do vetor é: {m:.1f}')
print(f'Existe(m) {c} elemento(s) abaixo da média')