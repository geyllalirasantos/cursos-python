#Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

c = 0
s = 0

n = int(input('Digite um valor [999] para parar: '))
while n != 999:
    n = int(input('Digite um valor [999 para parar]: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Você digitou {c} números.'
      f'A soma dos números foi de {s}!')