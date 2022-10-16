flag = 0
soma_geral = 0
cont_geral = 0
cont_faixa = 0
menor_idade = 1000

print('Digite a idade das pessoas visitantes do show.')
print('Obs: para encerrar, digite a idade 0')
idade = int(input('Idade: '))

while idade != flag:

    soma_geral += idade

    cont_geral += 1

    if idade >= 18 and idade <= 21:
        cont_faixa += 1

    if idade < menor_idade:
        menor_idade = idade
    
    idade = int(input('Idade: '))

media_geral = soma_geral / cont_geral
perc_faixa = cont_faixa / cont_geral * 100

print(f'\nMédia de idade do público: {media_geral:.0f} anos')
print(f'Porcentagem de pessoas com idade entre 18 e 21 anos: {perc_faixa:.1f}%')
print(f'Idade do visitante mais jovem: {menor_idade} anos')