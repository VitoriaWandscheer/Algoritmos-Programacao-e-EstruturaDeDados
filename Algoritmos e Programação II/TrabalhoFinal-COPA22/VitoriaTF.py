''' Vitória Wandscheer Pereira 
Turma Lidiane '''
''' Emerson de Lima Franco
Turma Rafael '''
'''Bsi 22'''

import time

''' Listas e Dicionários '''

todos_paises_cadastrados = []           # Lista com todos os países cadastrados
todas_abreviacoes_cadastradas = []      # Lista com todas as abreviações cadastradas
todos_grupos_cadastrados = []           # Lista com todos os grupos cadastrados
todos_jogos_cadastrados = []            # Lista com todos os jogos cadastrados

saldo_gols = {}     # Dicionário para armazenar a relação -> 'pais': nº de gols
faltas = {}         # Dicionário para armazenar a relação -> 'pais': nº de faltas

''' Procedimentos para preencher dicionários e listas '''

def informacoes_equipes():      # Adiciona chaves aos respectivos dicionarios e preenche listas com as informações das equipes
    with open('equipes.txt', 'r', encoding = 'utf-8') as equipes:
        
        for linha in equipes.readlines():
            linha_sem_quebra_de_linha = linha.replace('\n','')         # Remove \n
            lista_equipe = linha_sem_quebra_de_linha.split(';')        # Divide linha nos ; e armazena na lista ['grupo','abr','pais']

            saldo_gols[lista_equipe[2]] = 0                  # Cria uma chave com o nome do pais no dicionário gols e preenche com 0
            faltas[lista_equipe[2]] = 0                # Cria uma chave com o nome do pais no dicionário faltas e preenche com 0

            global todos_paises_cadastrados
            todos_paises_cadastrados.append(lista_equipe[2])       # adiciona pais à lista com os países cadastrados

            global todas_abreviacoes_cadastradas
            todas_abreviacoes_cadastradas.append(lista_equipe[1])   # adiciona abr à lista com as abreviações cadastradas

            global todos_grupos_cadastrados
            todos_grupos_cadastrados.append(lista_equipe[0])      # adiciona grupo à lista com os grupos cadastrados

def informacoes_jogos():        # Preenche os dicionarios 'gols' e 'faltas' com o número de gols por equipe(chave) e o numero de faltas por equipe(chave)
    with open('jogos.txt', 'r', encoding = 'utf-8') as jogos:
        for linha in jogos.readlines():
            linha_sem_quebras_de_linha = linha.replace('\n','') # Remove \n
            lista_jogo = linha_sem_quebras_de_linha.split(';') # Divide linha nos ; e armazena na lista ['pais 1', 'gols1', 'faltas1', 'pais2', 'gols2', 'faltas']

            if lista_jogo[0] in todos_paises_cadastrados:
                saldo_gols[lista_jogo[0]] = int(saldo_gols[lista_jogo[0]]) + (int(lista_jogo[1]) - int(lista_jogo[4]))
                faltas[lista_jogo[0]] = int(faltas[lista_jogo[0]]) + int(lista_jogo[2])
            
            if lista_jogo[3] in todos_paises_cadastrados:
                saldo_gols[lista_jogo[3]] = int(saldo_gols[lista_jogo[3]]) + (int(lista_jogo[4]) - int(lista_jogo[1]))
                faltas[lista_jogo[3]] = int(faltas[lista_jogo[3]]) + int(lista_jogo[5])

''' Procedimentos Auxiliares ''' 

def arquivos(): # Caso o arquivo ainda não exista ele é criado
    with open('jogos.txt', 'a', encoding = 'utf-8') as jogos:   # Caso não exista o arquivo 'jogos.txt' ele seja criado.
        controle = 0

    with open('equipes.txt', 'a', encoding = 'utf-8') as jogos:     # Caso não exista o arquivo 'equipes.txt' ele seja criado.    
        controle = 0

def menu(): # Mostra o menu na tela
    print()
    print('-' * LARGURA)
    print('MENU'.center(LARGURA))
    print('-' * LARGURA)
    print('[1] Sair')
    print('[2] Nova equipe')
    print('[3] Novo jogo')
    print('[4] Total de jogos')
    print('[5] Total de equipes')
    print('[6] Mostrar jogos cadastrados')
    print('[7] Pesquisar por país')
    print('[8] Apagar um jogo')
    print('-' * LARGURA)
    print('Informe a opção desejada:'.center(LARGURA))
    print('-' * LARGURA)

def nova_equipe(): # Recebe informações do usuário, se a equipe ainda não foi cadastrada, adiciona a nova equipe ao arquivo equipe.txt, caso contrario, avisa o usuário.
    
    print('*' * LARGURA)
    print('CADASTRAR NOVA EQUIPE'.center(LARGURA))
    print('*' * LARGURA)

    pais = input('Nome do País: ') # Recebe o nome do país do usuário
    while (pais.replace(' ', '').isalpha() == False) or (len(pais) < 3):         # Testa se o país (sem os espaços) está no alfabeto e se tem, no mínimo, 3 letras
        print('[!] Nome inválido. Tente novamente.')                             # Caso o nome esteja incorreto, solicita que a pessoa informe novamente
        pais = (input('Nome do País: '))                                         # Recebe o nome do país do usuário

    abr = (input('Abreviação: ')) # Recebe a abreviação do usuário
    while (abr.replace(' ', '').isalpha() == False) or (len(abr) != 3):     # Testa se a abreviação (sem os espaços) está no alfabeto e se tem 3 letras
        print('Abreviação deve conter 3 (três) letras. Tente novamente.')   # Caso o nome esteja incorreto, solicita que a pessoa informe novamente
        abr = (input('Abreviação: '))                                       # Recebe a abreviação do usuário

    grupo = (input('Grupo: ')) # Recebe o grupo do usuário
    while (grupo.replace(' ', '').isalpha() == False) or (len(grupo) != 1): # Testa se o grupo tem apenas uma letra
        print('Grupo deve conter apenas uma letra. Tente novamente.')       # Caso não tenha, solicita que a pessoa informe novamente
        grupo = (input('Grupo: '))                                          # Recebe o grupo do usuário

    print()

    time.sleep(0.6)
    print()
    print(f'Tem certeza'.center(LARGURA))   
    print(f'que deseja SALVAR a equipe?'.center(LARGURA)) # Questiona se a pessoa realmente deseja salvar a equipe informada.
    print()
    sim_nao()
    choice = input(' ') # Recebe do usuário a escolha
    time.sleep(0.6)

    while choice not in ['s','S','n','N']:  # Testa se choice é uma informação válida
        print()
        erro_simples()
        time.sleep(0.6)
        print()
        print(f'Tem certeza'.center(LARGURA))   
        print(f'que deseja SALVAR a equpe?'.center(LARGURA)) # Questiona se a pessoa realmente deseja salvar a equipe informada.
        print()
        sim_nao()
        choice = input(' ') # Recebe do usuário a escolha

    if choice == 'S' or choice == 's':   # Se o usuário escolher SALVAR a equipe...
        with open('equipes.txt', 'a+', encoding = 'utf-8') as equipes:
            informacoes_equipes()

            if pais.upper() not in todos_paises_cadastrados:
                equipes.write(f'{grupo.upper()};{abr.upper()};{pais.upper()}\n')
                print('EQUIPE CADASTRADA COM SUCESSO!\n'.center(LARGURA))
            else:
                print('x EQUIPE JÁ CADASTRADA x\n'.center(LARGURA))

    elif choice == 'N' or choice == 'n': # Se o usuário escolher NÃO SALVAR a equipe uma mensagem é apresentada, informando o não salvamento da paritda.
            linha_organizadora()
            print(f'Equipe NÃO foi salva.'.center(LARGURA))
            linha_organizadora()

    else:
        erro()

    # Salva informações no arquivo equipes.txt, caso ele não exista, será criado:

    

def novo_jogo(): # Adiciona novo jogo ao arquivo jogo.txt
    
    print('*' * LARGURA)
    print('CADASTRAR NOVO JOGO'.center(LARGURA))
    print('*' * LARGURA)
    print()

    print('Equipes:'.center(LARGURA))

    informacoes_equipes()

    pais1 = input('1ª equipe -> ')
    while (pais1.replace(' ', '').isalpha() == False) or (len(pais1) < 3):  # Testa se o país tem, no mínimo, 3 letras e se, sem os espaços, é alfabetico
        print('[!] Informaçao incorreta. Tente novamente.')                 # Caso não tenha, solicita que a pessoa informe novamente
        pais1 = input('-> ')                                                # Recebe o nome do país do usuário
    
    pais2 = input('2ª equipe -> ')
    while (pais2.replace(' ', '').isalpha() == False) or (len(pais2) < 3):   # Testa se o país tem, no mínimo, 3 letras e se, sem os espaços, é alfabetico
        print('[!] Informaçao incorreta. Tente novamente.')                 # Caso não tenha, solicita que a pessoa informe novamente
        pais2 = input('-> ')                                                # Recebe o nome do país do usuário

    if pais1.upper() not in todos_paises_cadastrados:       # Testa se o país esta cadastrado, caso contrario direciona para cadastrá-lo
        linha_organizadora()
        print(f'[!] {pais1.capitalize()} não está')
        print(f'cadastrado no banco COPA22.')
        print('Você será direcionado para cadastrá-lo.')
        linha_organizadora()
        nova_equipe()
        print('*' * LARGURA)

    if pais2.upper() not in todos_paises_cadastrados:       # Testa se o país esta cadastrado, caso contrario direciona para cadastrá-lo
        linha_organizadora()
        print(f'[!] {pais2.capitalize()} não está')
        print(f'cadastrado no banco COPA22.')
        print('Você será direcionado para cadastrá-lo.')
        linha_organizadora()
        nova_equipe()
        print('*' * LARGURA)

    print()
    print('Número de gols:'.center(LARGURA))

    gols1 = input(f'{pais1.capitalize()}: ')                    # Recebe o número de gols do país 1
    while gols1.isnumeric() == False:                           # Testa se gols1 não é um número
        print('[!] Informaçao incorreta. Tente novamente.')     # Mensagem de erro
        gols1 = input(f'{pais1.capitalize()}: ')                # Solicita que a pessoa informe novamente.

    gols2 = input(f'{pais2.capitalize()}: ')                    # Recebe o número de gols do país 2
    while gols2.isnumeric() == False:                           # Testa se gols2 não é um número
        print('[!] Informaçao incorreta. Tente novamente.')     # Mensagem de erro
        gols2 = input(f'{pais2.capitalize()}: ')                # Solicita que a pessoa informe novamente.

    print()
    print('Número de faltas:'.center(LARGURA))

    faltas1 = input(f'{pais1.capitalize()}: ')                  # Recebe o número de faltas do país 1
    while faltas1.isnumeric() == False:                         # Testa se faltas1 não é um número
        print('[!] Informaçao incorreta. Tente novamente.')     # Mensagem de erro
        faltas1 = input(f'{pais1.capitalize()}: ')              # Solicita que a pessoa informe novamente.

    faltas2 = input(f'{pais2.capitalize()}: ')                  # Recebe o número de faltas do país 2
    while faltas2.isnumeric() == False:                         # Testa se faltas2 não é um número
        print('[!] Informaçao incorreta. Tente novamente.')     # Mensagem de erro
        faltas2 = input(f'{pais2.capitalize()}: ')              # Solicita que a pessoa informe novamente.

    time.sleep(0.6)
    print()
    print(f'Tem certeza'.center(LARGURA))   
    print(f'que deseja SALVAR a partida?'.center(LARGURA)) # Questiona se a pessoa realmente deseja salvar a partida informada.
    print()
    sim_nao()
    choice = input(' ') # Recebe do usuário a escolha
    time.sleep(0.6)

    while choice not in ['s','S','n','N']:  # Testa se choice é uma informação válida
        print()
        erro_simples()
        time.sleep(0.6)
        print()
        print(f'Tem certeza'.center(LARGURA))   
        print(f'que deseja SALVAR a partida?'.center(LARGURA)) # Questiona se a pessoa realmente deseja salvar a partida informada.
        print()
        sim_nao()
        choice = input(' ') # Recebe do usuário a escolha

    if choice == 'S' or choice == 's':   # Se o usuário escolher SALVAR a partida...
        with open('jogos.txt', 'a+', encoding = 'utf-8') as jogos:  # Guarda as informações informadas pelo usuário no arquivo 'jogos.txt'
            jogos.write(f'{pais1.upper()};{int(gols1)};{int(faltas1)};{pais2.upper()};{int(gols2)};{int(faltas2)}\n')

    elif choice == 'N' or choice == 'n': # Se o usuário escolher NÃO SALVAR a partida uma mensagem é apresentada, informando o não salvamento da paritda.
            linha_organizadora()
            print(f'Partida NÃO foi salva.'.center(LARGURA))
            linha_organizadora()

    else:
        erro()

    print()

def mensagem_final(): # Mostra a mensagem final na tela.
    print('Encerrando...')
    print()
    time.sleep(1.5)
    print('*' * LARGURA)
    print('x PROGRAMA ENCERRADO x'.center(LARGURA))
    print('*' * LARGURA)
    print()

def erro(): # Mostra mensagem de erro na tela.  
    linha_organizadora()
    print(':('.center(LARGURA))    
    print()
    print('Opção inexistente, tente novamente!'.center(LARGURA))
    linha_organizadora()
    time.sleep(1.5)

def erro_simples(): # Mostra mensagem de erro na tela.
    print('[!] Informaçao incorreta.') # Mensagem de erro
    print('[!] Tente novamente:') # Mensagem de erro

def linha_organizadora():
    print()
    print('*' * LARGURA)
    print()

def sim_nao():
    print('[S] SIM')
    print('[N] NÃO')

''' Funções e Procedimentos chamados a partir da escolha do usuário no MENU '''

def add_equipe(): # Adiciona novas equipes, até que o usuário escolha não adicionar mais.
    nova_equipe()
    choice = 'S'
    while choice != 'N' or choice != 'n': # Verificar se o usuário deseja adicionar mais equipes, antes de retornar ao MENU.
        print('Continuar adicionando equipes?')
        sim_nao()
        choice = input(' ')
        if choice == 'S' or choice == 's':
            nova_equipe()
        elif choice == 'N' or choice == 'n':
            break
        else:
            erro()

def add_jogo(): # Adiciona novos jogos, até que o usuário escolha não adicionar mais.
    novo_jogo()
    choice = 'S'
    while choice != 'N' or choice != 'n': # Verificar se o usuário deseja adicionar mais jogos, antes de retornar ao MENU.
        print('Adicionar mais jogos?')
        sim_nao()
        choice = input(' ')
        if choice == 'S'or choice == 's':
            novo_jogo()
        elif choice == 'N' or choice == 'n':
            break
        else:
            erro()

def total_jogos(): # Mostra o total de jogos armazenados no banco COPA22 por meio da contagem de linhas no arquivo 'jogos.txt', uma vez que cada linha no arquivo corresponde a uma partida.
    
    total_linhas = 0

    with open('jogos.txt', 'r', encoding = 'utf-8') as jogos:   # Abre o arquivo para leitura
        for linha in jogos.readlines():                         # Efetua a contagem de linhas.
            total_linhas += 1
    
    if total_linhas == 0: # Caso não exista nenhum jogo cadastrado, será mostrada uma mensagem específica.
        linha_organizadora()
        print(f'Não há jogos cadastrados'.center(LARGURA))
        print(f'no banco COPA22.'.center(LARGURA))
        linha_organizadora()

    elif total_linhas == 1: # Caso exista apenas um jogo, será mostrada uma mensagem específica.
        linha_organizadora()
        print(f'Há {int(total_linhas)} jogo cadastrado'.center(LARGURA))
        print(f'no banco COPA22.'.center(LARGURA))
        linha_organizadora()

    else: # Caso exista mais de um jogo, será mostrada uma mensagem específica.
        linha_organizadora()
        print(f'Há {int(total_linhas)} jogos cadastrados'.center(LARGURA))
        print(f'no banco COPA22.'.center(LARGURA))
        linha_organizadora()

    time.sleep(1)

def total_equipes(): # Mostra o total de equipes armazenadas no banco COPA22 por meio da contagem de linhas no arquivo 'equipes.txt', uma vez que cada linha no arquivo corresponde a uma equipe.
    tot = 0

    with open('equipes.txt', 'r', encoding = 'utf-8') as equipes:   # Abre o arquivo para leitura
        for linha in equipes.readlines():                           # Efetua a contagem de linhas.
            tot += 1

    if tot == 0:    # Caso não exista nenhuma equipe cadastrada, será mostrada uma mensagem específica.
        linha_organizadora()
        print(f'Não há equipes cadastradas'.center(LARGURA))
        print(f'no banco COPA22.'.center(LARGURA))
        linha_organizadora()
        

    elif tot == 1:  # Caso exista apenas uma equipe, será mostrada uma mensagem específica.
        linha_organizadora()
        print(f'Há {tot} equipe cadastrada'.center(LARGURA))
        print(f'no banco COPA22.'.center(LARGURA))
        linha_organizadora()

    else:           # Caso exista mais de uma equipe, será mostrada uma mensagem específica.
        linha_organizadora()
        print(f'Há {tot} equipes cadastradas'.center(LARGURA))
        print(f'no banco COPA22.'.center(LARGURA))
        linha_organizadora()
    
    time.sleep(2)

def mostrar_jogos_cadastrados(): # Mostra os jogos armazenados no banco COPA22, caso não tenham jogos cadastrados apresenta uma mensagem com tal informação.
    
    print('*' * LARGURA)
    print('JOGOS CADASTRADOS:'.center(LARGURA))
    print('*' * LARGURA)

    global tot
    tot = 0 # Contador para verificar a quantidade de jogos
    id = 0 # Contador para registrar o id de cada partida
    
    with open('jogos.txt', 'r', encoding = 'utf-8') as jogos:   # Abre o arquivo para leitura.
        for linha in jogos.readlines():     # Efetua a contagem de linhas.
            tot += 1

    with open('jogos.txt', 'r', encoding = 'utf-8') as jogos:   # Abre o arquivo para leitura.
        if tot == 0:    # Caso não existam jogos cadastrados, será mostrada uma mensagem específica.
            linha_organizadora()
            print('Não há jogos cadastrados'.center(LARGURA))
            print('no banco COPA22.'.center(LARGURA))
            linha_organizadora()
            time.sleep(1)
            global auxiliar
            auxiliar = 0

        else:   # Se houverem jogos cadastrados, serão apresentados ao usuário.
            for linha in jogos.readlines(): # A cada linha do arquivo...
                
                linha = linha.replace('\n','')  # Remove a quebra de linha.
                lista = linha.split(';')    # Separa a linha a cada ; e armazena cada item em uma posição da lista.
                
                print('*'*LARGURA)
                print(f'Id Partida [{id}]') # Apresenta: o id da partida.
                print()
                print(f'{lista[0]} {lista[1]} X {lista[4]} {lista[3]}'.center(LARGURA)) # Apresenta: | Pais 1 | gols país 1| X | gols país 2 | Pais 2 |
                print()
                print('Faltas por equipe:')
                print(f'{lista[0]}: {lista[2]}')    # Apresenta: as faltas do País 1
                print(f'{lista[3]}: {lista[5]}')    # Apresenta: as faltas do País 2
                print()
                print(f'Total de faltas: {int(lista[2])+int(lista[5])}')  # Apresenta: o total de faltas da partida
                print()

                id += 1 # Contador para atualizar o id a cada partida
                time.sleep(1)

    linha_organizadora()
    time.sleep(1)

def pesquisa_pais(): # Permite que um usuário digite o nome de uma equipe(país) e retorna as informações referentes a tal equipe.

    pesquisa = input('Pesquisar: ').upper() # Recebe do usuário o país a ser pesquisado.

    informacoes_equipes()   # Chama a função 'informacoes_equipes()' para que a lista contendo todos os paises cadstrados seja preenchida.
    
    time.sleep(0.6)

    if pesquisa in todos_paises_cadastrados: # Caso a equipe pesquisada esteja na lista 'todos_paises_cadastrados'...
        linha_organizadora()
        print(f'{pesquisa}'.center(LARGURA))

        total_jogos_equipe_pesquisada = 0 # Contador para registrar a quantidade de jogos realizados pela equipe informada.

        with open('jogos.txt', 'r', encoding = 'utf-8') as jogos: # Abre o arquivo 'jogos.txt' para leitura.
            for partida in jogos.readlines(): # A cada linha de 'jogos'...
                if pesquisa in partida: # Se na partida há a equipe informada, apresenta os dados referentes a tal partida.
                    partida = partida.replace('\n','')
                    lista = partida.split(';')
                    linha_organizadora()
                    print(f'{lista[0]} {lista[1]} X {lista[4]} {lista[3]}'.center(LARGURA))
                    print()
                    print('Faltas por time:')
                    print()
                    print(f'{lista[0]}: {lista[2]}')
                    print(f'{lista[3]}: {lista[5]}')
                    total_jogos_equipe_pesquisada += 1
        
        if total_jogos_equipe_pesquisada == 0: # Caso não existam partidas registradas para tal equipe, apresenta a mensagem específica.
            linha_organizadora()
            print('Não há jogos cadastrados.'.center(LARGURA))

        else: # Caso contrario, apresenta os dados da equipe. 
            informacoes_jogos() # Chama a função 'jogos_armazenados()' para que os dicionários de cada informação (gols e faltas) sejam preenchidos.
            linha_organizadora()
            print(f'Saldo de gols:      {saldo_gols[pesquisa]}') # Apresenta o saldo de gols da equipe (saldo = gols a favor - gols contra).
            print(f'Total de faltas:    {faltas[pesquisa]} ')   # Apresenta o total de faltas cometidas pela equipe.

    else:
        linha_organizadora()
        print('Equipe não cadastrada.'.center(LARGURA))

    linha_organizadora()
    time.sleep(3)

def apagar_jogo():  # Permite que o usuário escolha uma das partidas cadastradas e apague-a.
    
    mostrar_jogos_cadastrados() # Mostra para o usuário os jogos amazenados, juntamente com seus respectivos id's.
    
    if auxiliar == 1: # Executa apenas se houverem jogos cadastrados no banco COPA22
        print('Informe o Id da partida'.center(LARGURA)) # Solicita que o usuário informe o id da partida que deseja remover.
        print('que deseja remover:'.center(LARGURA))
        apagar = input('-> ')  # Recebe do usuário o id da partida a ser apagada.

        while apagar.isnumeric() == False:  # Testa se o id da partida é um número, se não for, solicita que a pessoa informe novamente, até que seja um número.
            erro_simples()
            apagar = input('-> ')  # Recebe do usuário o id da partida a ser apagada.
        time.sleep(0.6)
        print()
        print(f'Tem certeza'.center(LARGURA))   
        print(f'que deseja APAGAR a partida [{apagar}]?'.center(LARGURA)) # Questiona se a pessoa realmente deseja apagar a partida escolhida.
        print()
        sim_nao()
        choice = input(' ') # Recebe do usuário a escolha
        time.sleep(0.6)

        while choice not in ['s','S','n','N']:  # Testa se choice é uma informação válida
            print()
            erro_simples()
            time.sleep(0.6)
            print()
            print(f'Tem certeza'.center(LARGURA))   
            print(f'que deseja APAGAR a partida [{apagar}]?'.center(LARGURA)) # Questiona se a pessoa realmente deseja apagar a partida escolhida.
            sim_nao()
            choice = input(' ') # Recebe do usuário a escolha.

        if choice == 'S' or choice == 's':   # Se o usuário escolher apagar a partida...
            with open('jogos.txt', 'r', encoding = 'utf-8') as jogos: # Abre o arquivo 'jogos.txt' para leitura.
                for partida in jogos.readlines(): # A cada partida em 'jogos'...
                    global todos_jogos_cadastrados  # Chama a lista global 'todos_jogos_cadastrados'.
                    todos_jogos_cadastrados.append(partida) # Adiciona cada partida a lista 'todos_jogos_cadastrados'.

            if int(apagar) < tot: # Verifica se o id escolhido está entre os existentes
                todos_jogos_cadastrados.pop(int(apagar)) # Utiliza o método pop para remover a partida específica da lista 'todos_jogos_cadastrados'.
                
                with open('jogos.txt', 'w', encoding = 'utf-8') as jogos: # Abre o arquivo 'jogos.txt' para escrita...
                    jogos.write('') # Sobrescrevendo o conteudo existente.

                with open('jogos.txt', 'a+', encoding = 'utf-8') as jogos: # Abre o arquivo 'jogos.txt', agora vazio, para escrita...
                    for indice in todos_jogos_cadastrados:  # A cada posição da lista...
                        jogos.write(indice) # Escreve, ao final do arquivo, a informação contida em tal posição, que corresponde a uma partida.
                
                linha_organizadora()
                print(f'PARTIDA [{apagar}] EXCLUIDA COM SUCESSO'.center(LARGURA))
                linha_organizadora()
            else:
                linha_organizadora()
                print(f'Partida [{apagar}] inexistente.'.center(LARGURA))
                print(f'Portanto, NÃO foi removida.'.center(LARGURA))
                linha_organizadora()

        elif choice == 'N' or choice == 'n': # Se o usuário escolher NÃO apagar a partida uma mensagem é apresentada, informando o não apagamento da paritda.
            linha_organizadora()
            print(f'Partida [{apagar}] NÃO foi removida.'.center(LARGURA))
            linha_organizadora()

        else:
            erro()
        
        time.sleep(1)

''' Principal '''

LARGURA = 40
auxiliar = 1
tot = 0
choice = 0

arquivos()  # Garante que, caso os arquivos utilizados ao longo do programa não existam, sejam criados.

while choice != 1: # Enquanto o usuário não escolher a opção [1] (Sair), o laço continuará sendo executado.

    menu()
    choice = input('-> ')  # Recebe a escolha do usuário
    print('-' * LARGURA)

    while choice.isnumeric() == False: # Testa se a escolha não é um número
        erro() # Mensagem de erro
        menu()
        choice = input('-> ') # Recebe a escolha do usuário
        print('-' * LARGURA)

    choice = int(choice)    # Transforma o dado informado do tipo string para o tipo inteiro

    time.sleep(0.6)

    if choice == 1:         # [1] Sair
        break

    elif choice == 2:       # [2] Nova equipe
        add_equipe()

    elif choice == 3:       # [3] Novo jogo
        add_jogo()

    elif choice == 4:       # [4] Total de jogos
        total_jogos()

    elif choice == 5:       # [5] Total de equipes
        total_equipes()

    elif choice == 6:       # [6] Relação de jogos e equipes
        mostrar_jogos_cadastrados()

    elif choice == 7:       # [7] Pesquisar por país
        pesquisa_pais()

    elif choice == 8:       # [8] Apagar um jogo
        apagar_jogo()

    else:                   # [?] Mensagem de erro
        erro()

mensagem_final()