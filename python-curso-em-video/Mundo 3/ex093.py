#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

jogador = dict()
partidas = list()


jogador['nome'] = str(input('Nome do jogador: '))
totalp = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, totalp):
    partidas.append(int(input(f'Quantos gols na {c+1}ª partida? ')))
print('-' * 40)
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print(jogador)
print('-' * 40)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-' * 40)
print(f'O jogador {jogador["nome"]} jogou {totalp} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    - Na partida {i+1} foram {v} gols.')
print(f'Somando um total de {jogador["total"]} gols.')