    # QUESTÃO 07 (População pais a ultrapassar pais b)

pais_a = 80000
pais_b = 200000
crescimento_a = 0.03
crescimento_b = 0.015
anos = 0

while pais_a < pais_b:
    pais_a = pais_a + (pais_a*crescimento_a)
    pais_b = pais_b + (pais_b*crescimento_b)
    anos += 1

print(f'Serão necessários {anos} anos para a população de A ultrapassar a população de B.')

print('\n\n\n=)')