    # QUESTÃO 2 (login e senha)

login = input('Informe um login:\n ')
senha = input('Informe uma senha:\n ')

MAX = 3
cont = 0

while cont < MAX:
    print('\n\nPara acessar o sistema digite os seguintes dados:\n ')
    login_dig = input('Login: ')
    senha_dig = input('Senha: ')

    if login == login_dig:
        if senha == senha_dig:
            print('Acesso Concedido!')
            cont += 3
        else:
            print('Senha incorreta!')
            cont += 1
    else:
        print('Login incorreto!')
        cont += 1

print('=)')