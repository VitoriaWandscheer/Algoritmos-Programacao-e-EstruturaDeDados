# Declare as seguintes variáveis:
# nome do funcionario, anoNascimento, numero de filhos, rg, salario, ativo.
# Atribua valores às respectivas variáveis.
# A variável ativo deverá receber um valor lógico.
# Mostre os dados conforme exemplo abaixo:
# O funcionário <<nome>> com rg <<rg>> possui <<>> anos de vida.
# O salario do funcionario << nome>> é de R$ << salario>> e possui << >> filhos.
# Situação ativo:<<ativo>>

print('Informe os seguintes dados do(a) funcionário: ')

nome_do_funcionario = str(input('Nome: '))
ano_de_nascimento = int(input('Ano de nascimento:'))
rg = int(input('RG: '))
numero_de_filhos = int(input('Nº de filhos: '))
salario = float(input('Salário: '))
ativo = 'Ativo'

ANO_ATUAL = 2022

anos = ANO_ATUAL - ano_de_nascimento

print(f'O(a) funcionário(a) {nome_do_funcionario}, com RG {rg}, possuí {anos} anos.\nO salário do(a) funcionario(a) {nome_do_funcionario} é de R${salario:.2f} e possui {numero_de_filhos} filhos.')

print('=)')