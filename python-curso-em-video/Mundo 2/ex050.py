#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

s = 0
cont = 0

for n in range(1, 7):
    n = int(input(f'Digite o {n}º valor: '))

    if n % 2 == 0:
        cont += 1
        s += n
print(f'Você informou {cont} VALORES PARES\nA soma valores é {s}')