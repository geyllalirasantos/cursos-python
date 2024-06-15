#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação.
#depois mostre:
#1- apenas os 5 primeiros colocados
#2- os últimos 4 colocados
#3- lista com os times em ordem alfabética (SORT)
#4- em que posição na tabela está o time da Chapecoense

brasileirao = (
    'Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo',
    'Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza',
    'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco',
    'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG'
)

ordem = sorted(brasileirao)

print(f'BRASILEIRÃO 2023\n'
      f'{brasileirao}')
print('-' * 50)
print(f'Os 5 primeiros colocados do Brasileirão são:\n'
      f'{brasileirao[:5]}')
print('-' * 50)
print(f'Os 4 últimos colocados são:\n'
      f'{brasileirao[-4:]}')
print('-' * 50)
print(f'Times do Brasileirão em ordem alfabética:\n'
      f'{ordem}')