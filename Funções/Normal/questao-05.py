# 30/12/2022

def media(nota1, nota2, nota3):
    '''Função que recebe como parâmetros 3 notas do aluno e retorna a sua média (aritmética).'''
    return (nota1 + nota2 + nota3) / 3

def conceito(media):
    '''Função que receba como parâmetro a média do aluno e retorna o seu conceito'''
    if media >= 8:
        return 'A'
    elif media >= 5:
        return 'B'
    else:
        return 'C'

#Programa principal
print('Informe 3 notas');
n1 = str(float(input('1ª nota:')))
n2 = str(float(input('2ª nota:')))
n3 = str(float(input('3ª nota:')))
med = media(n1,n2,n3)
conc = conceito(med)
print(f'\nA média é: {med:.1f}')
print(f'O conceito é: {conc}')