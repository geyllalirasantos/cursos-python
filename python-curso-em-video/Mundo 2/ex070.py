#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

total = 0
maismil = 0
menor = 0
cont = 0
barato = ' '

print('-----ESTATÍSTICA DE PRODUTOS-----')
while True:
    prod = str(input('Produto: ')).strip()
    preco = float(input('Preço (sem ponto ou vírgula): R$'))
    cont += 1
    print('-' * 40)

    total += preco

    if cont == 1 or preco < menor:
        menor = preco
        barato = prod
    #else:
    #    if preco < menor:
    #        menor = preco
    #        barato = prod


    if preco >= 1000:
        maismil += 1


    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar[S/N]? ')).upper().strip()[0]
        print('-' * 40)
    if resp == 'N':
        break

print(f'O total gasto na compra é {total:.2f}\n'
      f'{maismil} produtos custam mais de R$1000.00\n'
      f'O produto mais barato é {barato}, que custa R${menor}')