#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

print('-=' * 20)
print('SEVIÇO DE ALISTAMENTO MILITAR')
print('-=' * 20)
ano = int(input('Qual ano você nasceu: '))

idade = date.today().year - ano

if idade == 18:
   print('Você faz 18 anos este ano. Você precisa se alistar!')
elif idade < 18:
    print(f'Ainda faltam {idade} ano(s)')
elif idade > 18:
    print(f'Você já passou do tempo de alistamento há {idade - 18} ano(s)')