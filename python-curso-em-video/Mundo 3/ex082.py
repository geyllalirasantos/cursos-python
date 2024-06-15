#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.

numeros = list()
impar = list()
par = list()

while True:
    n = int(input('Digite um valor: '))

    if n not in numeros:
        numeros.append(n)

    if n % 2 == 0:
        par.append(n)
    elif n % 2 == 1:
        impar.append(n)

    choice = str(input('Quer continuar[S/N]? ')).upper().strip()[0]
    if choice in 'N':
        break

print('-' * 40)
print(f'A lista completa é: {numeros}')
print(f'A lista de pares é: {par}')
print(f'A lista de ímpares é: {impar}')