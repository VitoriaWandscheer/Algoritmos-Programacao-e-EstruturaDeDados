print('Olá, informe os seguintes dados para a contrução da escada:')

a_degrau = float(input('Altura do degrau: '))
a_construcao = float(input('Altura que desja alcançar: '))

n_degraus = a_construcao / a_degrau

print(f'Para alcançar {a_construcao} metros com degraus de {a_degrau} metros, serão necessários {n_degraus:.1f} degraus.')

print('=)')