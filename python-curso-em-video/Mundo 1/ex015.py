#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dias com o carro? '))
km = float(input('Quantos KM rodados? '))
preco = (dias*60) + (km*0.15)
print(f'O aluguel do carro por {dias} dias e {km:.2f} KM rodados custou R${preco}')