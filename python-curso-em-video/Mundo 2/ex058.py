#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
numero = random.randint(0,10) #sorteio do n pelo computador
c = 0
n = 0


while n != numero:
    n = int(input('Digite um número de 0 a 10: '))

    if n!= numero:
        n = print('Não foi esse número que pensei... Tente novamente.\n'
                  'Digite um número: ')
        c += 1
    else:
        print('-=' * 20)
        print(f'Parabéns! {n} também foi o número escolhido pela máquina')
        print(f'Você levou {c} tentaivas para acertar')