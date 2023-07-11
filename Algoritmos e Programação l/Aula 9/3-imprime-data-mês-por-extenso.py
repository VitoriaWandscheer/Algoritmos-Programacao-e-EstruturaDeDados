# Faça um programa que leia uma data de nascimento no formato dd/mm/aaaa
# e imprima a data com o mês escrito por extenso.
# Exemplo: Data = 20/02/1995 
# Resultado gerado pelo programa: Você nasceu em 20 de fevereiro de 1995

data = str(input('Informe sua data de nascimento no seguinte formato:\ndd/mm/aaaa\n'))

num = data[3]+data[4]

if num == '01':
    print('Você nasceu em',data[0]+data[1],'de janeiro de', data[6]+data[7]+data[8]+data[9])
elif num == '02':
    print('Você nasceu em',data[0]+data[1],'de fevereiro de', data[6]+data[7]+data[8]+data[9])
elif num == '03':
    print('Você nasceu em',data[0]+data[1],'de março de', data[6]+data[7]+data[8]+data[9])
elif num == '04':
    print('Você nasceu em',data[0]+data[1],'de abril de', data[6]+data[7]+data[8]+data[9])
elif num == '05':
    print('Você nasceu em',data[0]+data[1],'de maio de', data[6]+data[7]+data[8]+data[9])
elif num == '06':
    print('Você nasceu em',data[0]+data[1],'de junho de', data[6]+data[7]+data[8]+data[9])
elif num == '07':
    print('Você nasceu em',data[0]+data[1],'de julho de', data[6]+data[7]+data[8]+data[9])
elif num == '08':
    print('Você nasceu em',data[0]+data[1],'de agosto de', data[6]+data[7]+data[8]+data[9])
elif num == '09':
    print('Você nasceu em',data[0]+data[1],'de setembro de', data[6]+data[7]+data[8]+data[9])
elif num == '10':
    print('Você nasceu em',data[0]+data[1],'de outubro de', data[6]+data[7]+data[8]+data[9])
elif num == '11':
    print('Você nasceu em',data[0]+data[1],'de novembro de ', data[6]+data[7]+data[8]+data[9])
elif num == '12':
    print('Você nasceu em',data[0]+data[1],'de dezembro de ', data[6]+data[7]+data[8]+data[9])
else:
    print('ERRO')

print('=)')