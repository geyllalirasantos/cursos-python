#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = 0
c = 0
sm = 0

n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    c+=1
    sm += n
    n = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {c} números.\n'
      f'A soma entre eles foi de {sm}.')