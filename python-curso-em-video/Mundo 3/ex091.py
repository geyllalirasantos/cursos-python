#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogo = dict()
for c in range(1,5):
    jogo[f'jogador{c}']=randint(1,6)

ranking = list()

print('VALORES SORTEADOS:')
for k, v in jogo.items():
    sleep(1)
    print(f'O {k} tirou {v} no dado.')
print('-' * 40)

print('RANKING DOS JOGADORES:')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
      print(f'{i+1}º lugar: O {v[0]} com {v[1]}.')
      sleep(1)