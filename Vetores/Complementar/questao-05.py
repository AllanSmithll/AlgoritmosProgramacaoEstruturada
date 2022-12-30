# 30/12/2022

na = 3  #Número de apostadores (testando para apenas 3 apostadores ao invés de 20)

nda = 8  #Número de dezenas apostadas por cada 

vda = [None]*nda  #Vetor que irá conter as dezenas apostadas por um apostador

vds = [6,7,13,14,26]  #Vetor que contém as dezenas sorteadas
nds = len(vds) #Número de dezenas sorteadas

for i in range(na):

    #lendo as dezenas de um apostador
    print(f'\nDezenas do Apostador {i+1}:')
    for j in range(nda):
        vda[j] = int(input())

    #verificando se a aposta é válida
    valida = True
    for j in range(nda):
        #verificando se a dezena está entre 1 e 80
        if vda[j] < 1 or vda[j] > 80:
            valida = False
            break
        #verificando se há dezena repetida
        repetida = False
        for k in range(nda):
            if vda[j] == vda[k] and j != k:
                repetida = True
                break
        if repetida:
            valida = False

    #contando a quantidade de acertos se a aposta for válida 
    if valida:
        cont = 0
        for j in range(nda):
            for k in range(nds):
                if vda[j] == vds[k]:
                    cont += 1
        print(f'Número de acertos: {cont}')
    else:
        print('Aposta inválida')   