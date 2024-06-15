#Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

cadastro = dict()
lista = list()
soma = media = 0

while True:
    cadastro.clear()
    cadastro['nome'] = str(input('Nome: '))
    while True:
        cadastro['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if cadastro['sexo'] in'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    cadastro['idade'] = int(input('Idade: '))
    soma += cadastro['idade']
    lista.append(cadastro.copy())

    while True:
        choice = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
        if choice in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if choice == 'N':
        break

#print('-' * 40)
#print(lista)
print('-' * 40)
print(f'A) Foram cadastradas {len(lista)} pessoas.')
media = soma / len(lista)
print(f'B) A média de idade entre os cadastrados é de {media:5.2f} anos.')
print(f'C) As mulheres casastradas foram ', end='')
for p in lista:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]},', end=' ')
print()
print(f'D) Lista das pessoas que tem idade acima da média:')
for p in lista:
    if p['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
print()
print('-----PROGRAMA ENCERRADO-----')