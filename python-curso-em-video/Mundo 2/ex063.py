#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
#0 – 1 – 1 – 2 – 3 – 5 – 8

print('SEQUÊNCIA FIBONACCI')
n = int(input('Quantos termos você quer mostrar? '))

t1 = 0
t2 = 1
c=3
print(f'{t1} - {t2}', end='')

while c <= n:
    t3 = t1 + t2
    print(f' - {t3}', end='')
    t1 = t2
    t2 = t3
    c +=1
print(' - FIM')