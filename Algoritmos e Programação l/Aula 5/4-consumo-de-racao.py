# Pedro comprou um saco de ração, com peso em quilos.
# Ele possui dois gatos, para os quais fornece a quantidade de ração em gramas.
# A quantidade diária de ração fornecida para cada gato é sempre a mesma.
# Faça um programa que receba
# o peso do saco de ração e a quantidade de ração fornecida para cada gato,
# calcule e mostre quanto restará de ração no saco após 5 dias de consumo.

qtd_racao = float(input('Informe o peso do saco de ração: '))
qtd_gato_a = float(input('Informe quantas gramas são fornecidas para o primeiro gato: '))
qtd_gato_b = float(input('Informe quantas gramas são fornecidas para o segundo gato: '))

qtd_apos_cinco_dias = (qtd_racao * 1000) - (5 * qtd_gato_a) - (5 * qtd_gato_b)

print(f'Após cinco dias de consumo a quantidade de ração que restrá será de {qtd_apos_cinco_dias} gramas.')

print('=)')