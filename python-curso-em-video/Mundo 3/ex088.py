#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
mega = []
jogos = []

print('------- GERADOR DA MEGA SENA -------')
quant = int(input('Quantos jogos você quer fazer? '))
total = 1
while total <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in mega:
            mega.append(num)
            cont += 1
        if cont >= 6:
            break
    mega.sort()
    jogos.append(mega[:])
    mega.clear()
    total += 1

print('-' * 40)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')