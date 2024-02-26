#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

maior18 = 0
homem = 0
mulher20 = 0

while True:
    print(f'-----CADASTRO-----')
    idade = int(input('Idade: '))
    while idade < 0:
        idade = int(input('Condição inválida. \n'
                         'Idade: '))

    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    print('-' * 40)
    while sexo not in 'MF':
        sexo = str(input('Condição inválida. \n'
                         'Sexo [M/F]: ')).upper().strip()[0]

    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1

    choice = str(input('Quer continuar[S/N]? ')).upper().strip()[0]
    print('-' * 40)
    while choice not in 'SN':
        choice = str(input('Condição inválida. \nQuer continuar[S/N]? ')).upper().strip()[0]
    if choice == 'N':
            break

print('-----FIM DE CADASTRO-----')
print(f'Foram cadastrados: \n'
      f'- {maior18} pessoas maiores de 18 anos. \n'
      f'- {homem} homens.\n'
      f'- {mulher20} mulheres com menos de 20 anos.')