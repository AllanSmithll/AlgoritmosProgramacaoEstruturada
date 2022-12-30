# 30/12/2022 - Data de publicação no Github

email = input('Digite o email: ')
email_separado = email.split('@')
login = email[0]
dominio = email[1]

print(f'Login: {email_separado[0]}')
print(f'Domínio: {email_separado[1]}')