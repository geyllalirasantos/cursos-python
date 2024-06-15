#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. 
#No final, mostre:                                                                                                    
#- Quantas pessoas foram cadastradas.                                                                                                               
#- Uma listagem com as pessoas mais pesadas.                                                                                                    
#- Uma listagem com as pessoas mais leves.

dado = []
galera = []
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))

    if len(galera) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]

    galera.append(dado[:])
    dado.clear()

    choice = str(input('Quer continuar[S/N]? ')).upper().strip()[0]
    if choice in 'N':
        break
print()
print('-' * 40)
print(f'Você cadastrou {len(galera)} pessoas.')
print(f'Maior peso foi {maior}')
print('Peso de ', end=' ')
for p in galera:
    if p[1] == maior:
        print(f'{p[0]}', end='')
print()
print(f'Menor peso {menor}')
print('Peso de ', end='')
for p in galera:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')