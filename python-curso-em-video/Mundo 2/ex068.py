#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random
computador = random.randint(0, 20)
v = 0

print('VAMOS JOGAR PAR OU ÍMPAR')
print('-' * 40)

while True:
    n = int(input('Digite um valor: '))
    total = n + computador
    tipo = ' '

    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? [P/I] ')).upper().strip()[0]
    print(f'Você jogou {n} e o computador jogou {computador}. \nTotal de {total}. ', end='')
    print(f'DEU PAR.' if total % 2 == 0 else 'DEU ÍMPAR.')

    if tipo == 'P':
        if total % 2 == 0:
            print('Você GANHOU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você GANHOU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente... ')

print('-----GAME OVER!-----')
print(f'Você venceu {v} vezes.')