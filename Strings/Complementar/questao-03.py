# 30/12/2022

nome = input('Nome:\n')
vetor = nome.split()
saida = vetor[-1]+', '

for i in range(len(vetor) - 1):
    saida += vetor[i][0]+'. '

print(saida)