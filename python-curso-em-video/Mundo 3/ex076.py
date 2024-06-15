#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

lista = ('Biscoito', 2.30,
         'Salgadinho', 3,
         'Refrigerante', 2,
         'Sanduíche', 5)

print('-' * 40)
print(f'{"CANTINA DO ACAMP":^40}')
print('-' * 40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<33}', end='')
    else:
        print(f'R${lista[pos]:>5.2f}')
print('-' * 40)