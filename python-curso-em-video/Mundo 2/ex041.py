#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

from datetime import date

ano = int(input('Digite o ano do seu nascimento: '))

idade = date.today().year - ano

print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Atleta da categoria MIRIM')
elif idade > 9 and idade <= 14:
    print('Atleta da categoria INFANTIL')
elif idade > 14 and idade <= 19:
    print('Atleta da categoria JUNIOR')
elif idade <= 25:
    print('Atleta da categoria SÊNIOR')
elif idade > 25:
    print('Atleta da categoria MASTER')