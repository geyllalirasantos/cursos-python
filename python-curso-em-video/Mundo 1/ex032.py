#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
ano = int(input('Qual ano você quer analisar? \nColoque 0 para analisar o ano atual '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
# o ano tem que ser divisivel por quarto / não pode ser divisivel por 100 OU ser divisivel por 400
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} não é BISSEXTO.')