#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

c = 0
sm = 0
maior = 0
menor = 0
choice = 'S'

while choice == 'S':
    n = int(input('Digite um número: '))
    choice = str(input('Quer continuar[S/N]? ')).upper().strip()[0]

    #O primeiro N precisa ser o referencial das comparações
    #Verifica se é a primeira execução do loop
    if c == 0:
        maior = menor = n

    if n > maior:
        maior = n
    elif n < menor:
        menor = n

    c += 1
    sm += n

media = (sm / c)
print('~' * 30)
print(f'Você digitou {c} números.\n'
      #f'soma {sm}\n'
      f'A média entre os valores foi {media:.2f}\n'
      f'O maior valor foi {maior} e o menor foi {menor}')