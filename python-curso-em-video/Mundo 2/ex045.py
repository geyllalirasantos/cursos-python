#Crie um programa que faça o computador jogar Jokenpô com você.

import random
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0,2)

print('SUAS OPÇÕES:\n'
      '[ 0 ] PEDRA\n'
      '[ 1 ] PAPEL\n'
      '[ 2 ] TESOURA')
jogador = int(input('Qual é a sua jogada? '))
print('-' * 22)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-' * 22)

if computador == 0: #computador jogou PEDRA
      if jogador == 0:
            print('EMPATE')
      elif jogador == 1:
            print('JOGADOR GANHOU')
      elif jogador == 2:
            print('COMPUTADOR GANHOU')
      else:
        print('JOGADA INVÁLIDA')

elif computador == 1: #computador jogou PAPEL
      if jogador == 0:
            print('COMPUTADOR GANHOU')
      elif jogador == 1:
            print('EMPATE')
      elif jogador == 2:
            print('JOGADOR GANHOU')
      else:
            print('JOGADA INVÁLIDA')

elif computador == 2: # computador jogou TESOURA
      if jogador == 0:
            print('JOGADOR GANHOU')
      elif jogador == 1:
            print('COMPUTADOR GANHOU')
      elif jogador == 2:
            print('EMPATE')
      else:
            print('JOGADA INVÁLIDA')

else:
      print('JOGADA INVÁLIDA')