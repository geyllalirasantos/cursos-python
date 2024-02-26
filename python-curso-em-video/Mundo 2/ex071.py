#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('-' * 30)
print(f'BANCO')
print('-' * 30)
valor = int(input('Digite o valor do saque: R$'))
total = valor
ced = 50
tced = 0

while True:
    if total >= ced:
        total -= ced
        tced += 1
    else:
        if tced > 0:
            print(f'Total de {tced} cédulas de R${ced}')
            if ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 1:
                ced = 1
            tced = 0
            if total == 0:
                break
print('-' * 30)
print('Volte sempre!')