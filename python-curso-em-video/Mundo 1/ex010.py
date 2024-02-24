#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Digite o valor em real: R$'))
dolar = real / 4.87
print(f'R${real:.2f} equivale a US${dolar:.2f}')