# 30/12/2022 -> Data que pus no GitHub

uf = ['AC','AL','AM','AP','BA','CE','DF','ES','GO','MA','MG','MS','MT','PA','PB','PE','PI','PR','RJ','RN','RO','RR','RS','SC','SE','SP','TO']
n = len(uf)
cont = [0]*n

while True:
    voto = input('Digite a UF de sua preferência: ').upper()
    for i in range(n):
        if uf[i] == voto:
            cont[i] += 1
            break
    else:
        break    

maior = cont[0]
for i in range(1,n):
    if cont[i] > maior:
        maior = cont[i]

print('\nUF mais votada:')
for i in range(n):
    if cont[i] == maior:
        print(f'{uf[i]} com {cont[i]} votos')