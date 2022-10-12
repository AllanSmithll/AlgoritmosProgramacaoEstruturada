# Dizer qual caracter é aquele que é digitado no input

entrada = input('Caracter: ')

caracter = entrada.lower()

if caracter >= 'a' and caracter <= 'z':
    if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u':
        tipo = 'vogal'
    else:
        tipo = 'consoante'
else:
    if caracter >= '0' and caracter <= '9':
        tipo = 'número'
    else:
        tipo = 'caracter especial'   

print(f'Tipo: {tipo}') 