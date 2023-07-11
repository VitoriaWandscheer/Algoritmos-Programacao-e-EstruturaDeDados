    # QUESTÃO 4 (maior e menor temp. media das temp e total de temp)

print('Informe as temperaturas:\n (Quando encerrarem os valores digite "FIM")')
temperatura = str(input('= '))

COND = 'FIM'

if temperatura.upper() != COND:
    temp = int(temperatura) 
    maior_valor = temp
    menor_valor = temp
    n_temp = 1
    s_temp = temp

    while temperatura.upper() != COND:
        temperatura = str(input('= '))
        if temperatura.upper() != COND:
            temp = int(temperatura) 
            n_temp = n_temp + 1
            s_temp = s_temp + (temp)
            if temp > maior_valor:
                maior_valor = temp
            elif temp < menor_valor:
                menor_valor = temp

    media_temp = s_temp / n_temp

    print(f'\n\nForam lidas {n_temp} temperaturas.')
    print(f'A média das temperaturas informadas é {media_temp:.2f} graus.')
    print(f'A menor temperatura foi {menor_valor} graus.')
    print(f'A maior temperatura foi {maior_valor} graus.')
else:
    print( '\n\n\nNão foram informadas temperaturas para análise.')

print('\n\n\n=)')