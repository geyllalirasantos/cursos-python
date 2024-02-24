#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math
num = float(input('Digite um valor: '))
print(f'O número digitado foi {num} e sua parte inteira é {(math.trunc(num))}')