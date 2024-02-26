#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros

preco = float(input('Preço das compras? R$ '))
pgmt = int(input('Forma de pagamento\n'
                 '1 - à vista (dinheiro ou pix)\n'
                 '2 - à vista no cartão\n'
                 '3 - 2x  no cartão\n'
                 '4 - 3x ou mais no cartão\n'))
print('.' * 20)
print('CALCULANDO....')
print('.' * 20)

if pgmt == 1:
    desc1 = preco - (preco * 10 / 100)
    print(f'O seu produto com pagamento à vista no dinheiro ou pix tem desconto de 10%\n'
          f'Agora ele custa R${desc1:.2f}!')
elif pgmt == 2:
    desc2 = preco - (preco * 5 / 100)
    print(f'O seu produto com pagamento à vista no cartão tem desconto de 5%\n'
          f'Agora ele custa  R${desc2:.2f}')
elif pgmt == 3:
    print(f'O seu produto não tem desconto, nem acrescimo.\n'
          f'O valor da sua compra é de R${preco:.2f}')
elif pgmt == 4:
    acr = preco + (preco * 20 / 100)
    print(f'O seu produto com pagamento em 3x ou mais no cartão de crédito tem acrescimo de 20%\n'
          f'Agora ele custa R${acr:.2f}')
else:
    print('OPÇÃO INVÁLIDA DE PAGAMENTO')