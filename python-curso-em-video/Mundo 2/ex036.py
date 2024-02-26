#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('-' * 20)
print('SIMULADOR DE EMPRÉSTIMO BANCÁRIO')
print('-' * 20)
casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))


prestacao = casa / (anos *12)
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos, a prestação será de R${prestacao:.2f}')

minimo = salario * 30 / salario

if prestacao <= minimo:
    print('Seu empréstimo foi aprovado!')
else:
    print('Sua empréstimo foi negado')