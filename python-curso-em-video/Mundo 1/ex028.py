#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
numero = random.randint(0,5) #sorteio do n pelo computador

n = int(input('Digite um número de 0 a 5: '))
if n == numero:
    print(f'Parabéns! {n} também foi o número escolhido pela máquina')
else:
    print('Tente novamente')