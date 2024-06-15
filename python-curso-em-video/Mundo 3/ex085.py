#Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

numeros = [[],[]]
valor = 0
for n in range(1,8):
    valor = (int(input(f'Digite o {n}º valor: ')))
    if valor % 2 == 1:
        numeros[0].append(valor)
    if valor % 2 == 0:
        numeros[1].append(valor)

print('-' * 40)
numeros[0].sort()
numeros[1].sort()
#print(f'Os valores digitados foram {numeros}')
print(f'Os números ímpares foram {numeros[0]}')
print(f'Os números pares foram {numeros[1]}')