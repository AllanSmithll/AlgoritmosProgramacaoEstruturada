# 30/12/2022 -> Questão Única

while True:
  verbo = str.lower(input('Digite um verbo no infinitivo: '))
  tam = len(verbo) #tamanho
  rad = verbo[:tam-2] #radical
  vogal_tematica = verbo[tam-2]
  if vogal_tematica == 'a':
      print('\nPresente:')
      print(f'Eu {rad}o')
      print(f'Tu {rad}as')
      print(f'Ele/Ela {rad}a')
      print(f'Nós {rad}amos')
      print(f'Vós {rad}ais')
      print(f'Eles/Elas {rad}am')

  elif vogal_tematica == 'e':
      print('\nPresente:')
      print(f'Eu {rad}o')
      print(f'Tu {rad}es')
      (f'Ele/Ela {rad}e')
      print(f'Nós {rad}emos')
      print(f'Vós {rad}eis')
      print(f'Eles/Elas {rad}em')

  elif vogal_tematica == 'i':
      print('\nPresente:')
      print(f'Eu {rad}o')
      print(f'Tu {rad}es')
      print(f'Ele/Ela {rad}e')
      print(f'Nós {rad}imos')
      print(f'Vós {rad}is')
      print(f'Eles/Elas {rad}em')

  resp = input('\nQuer conjugar mais um verbo (S/N): ').upper()
  if resp == 'N':
      break
  print()