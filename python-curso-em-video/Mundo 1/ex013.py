#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual o salário do funcionário? R$'))
novo = salario + (salario*15/100)
print(f'Com o ajuste de 15%, o salário agora custa R${novo:.2f}')

'''
#teste com 5% desconto à vista e 8% de aumento no cartão
preco = float(input('Qual o preço do produto? R$'))
dinheiro = preco - (preco*5/100)
cartao = preco + (preco*8/100)
print('-' * 15)
print(f'O produto de preço R${preco:.2f} sai por R${dinheiro:.2f} à vista e R${cartao:.2f} no cartão')
'''