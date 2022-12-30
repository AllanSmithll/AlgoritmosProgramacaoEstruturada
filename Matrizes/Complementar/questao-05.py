# 30/12/2022

m = [0,15,30,5,12],[15,0,10,17,28],[30,10,0,3,11],[5,17,3,0,80],[12,28,11,80,0]

ordem = 5

soma = 0
print('\nDigite as cidades do percurso (ou 0 para sair)')
orig = int(input())
while True:
    dest = int(input())
    if dest == 0:
        break
    soma += m[orig-1][dest-1]
    orig = dest

print(f'\nDistancia percorrida: {soma} km')