#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = list()
while True:
    n = int(input('Digite um valor: '))

    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado. Não vou adicionar.')

    choice = str(input('Quer continuar[S/N]? ')).upper().strip()[0]
    if choice in 'N':
        break

print('-' * 40)
print(f'Você digitou os valores {numeros.sort()}.')




'''    
    valores.append(int(input('Digite um valor: ')))

    if valores in valores:
        print('Valor duplicado! Não vou adicionar.')

    choice = str(input('Quer continuar[S/N]? ')).upper().strip()[0]
    print('-' * 40)
    while choice not in 'SN':
        choice = str(input('Condição inválida. \nQuer continuar[S/N]? ')).upper().strip()[0]
    if choice == 'N':
        break

print('-' * 40)
print(f'Você digitou os valores {valores.sort()}.')
'''