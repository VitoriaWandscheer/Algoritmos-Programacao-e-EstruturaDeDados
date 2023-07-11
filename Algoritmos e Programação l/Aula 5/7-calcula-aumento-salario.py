# Faça um programa que receba
# o código correspondente ao cargo de um funcionário e seu salário atual
# e mostre o cargo, o valor do aumento e seu novo salário.
# Os cargos estão na tabela a seguir:
# Código    Cargo           % de Aumento
#   1       Escrituario         50%
#   2       Secretario          35%
#   3       Caixa               20%
#   4       Gerente             10%
#   5       Diretor             NT

cargo = int(input('Informe o código do funcionário: '))
s_atual = float(input('Informe o salario atual do funcionário: '))

PORCENT_UM = 0.5
PORCENT_DOIS = 0.35
PORCENT_TRES = 0.2
PORCENT_QUATRO = 0.1

if cargo == 1 : 
    valor_aum = s_atual * PORCENT_UM
    s_novo = s_atual + valor_aum
    print(f'O escrituário terá um aumento de R${valor_aum:.2f}.\nSeu novo salário será de R${s_novo:.2f}')

if cargo == 2 : 
    valor_aum = s_atual * PORCENT_DOIS
    s_novo = s_atual + valor_aum
    print(f'O secretário terá um aumento de R${valor_aum:.2f}.\nSeu novo salário será de R${s_novo:.2f}')

if cargo == 3 : 
    valor_aum = s_atual * PORCENT_TRES
    s_novo = s_atual + valor_aum
    print(f'O caixa terá um aumento de R${valor_aum:.2f}.\nSeu novo salário será de R${s_novo:.2f}')

if cargo == 4 : 
    valor_aum = s_atual * PORCENT_QUATRO
    s_novo = s_atual + valor_aum
    print(f'O gerente terá um aumento de R${valor_aum:.2f}.\nSeu novo salário será de R${s_novo:.2f}')

if cargo == 5 : 
    print(f'O diretor não terá aumento.\nSeu salário continuará sendo R${s_atual:.2f}')

print('=)')