# 30/12/2022

na = 20
nn = 3
mat = [[None]*(nn+1) for i in range(na)]

print('Digite as notas dos alunos')
for lin in range(na):
    print(f'\n{lin+1}º ALUNO:')
    for col in range(nn):
        mat[lin][col] = float(input(f'{col+1}ª Nota: '))

for lin in range(na):
    mat[lin][nn] = (mat[lin][0] + mat[lin][1] + mat[lin][2]) / nn 

print('\n          1ª NOTA  2ª NOTA  3ª NOTA    MÉDIA')
for lin in range(na):
    print(f'{lin+1}º ALUNO',end='')
    for col in range(nn+1):
        print(f'{mat[lin][col]:9.1f}',end='')
    print()

soma = 0
for lin in range(na):
    soma += mat[lin][nn]
media = soma / na
print(f'\nMédia geral da turma: {media:.1f}')

cont = 0
for lin in range(na):
    if mat[lin][nn] > media:
        cont += 1
print(f'\nNúmero de alunos com média superior à média geral da turma: {cont}')