flag = 0

print(f'Informe os dados dos alunos. Para encerrar, digite a matrícula {flag}.')
mat = int(input('\nMatrícula: '))

while mat != flag:

    nome = input('Nome: ')
    nota1 = float(input('1ª Nota: '))
    nota2 = float(input('2ª Nota: '))
    media = (nota1 + nota2) / 2

    if media >= 7.0:
        sit = 'Aprovado'
    else:
        sit = 'Reprovado'

    print(f'\nMatrícula: {mat}')
    print(f'Nome: {nome}')
    print(f'Média: {media:.1f}')
    print(f'Situação: {sit}')

    mat = int(input('\nMatrícula: '))

print('Fim do programa.')