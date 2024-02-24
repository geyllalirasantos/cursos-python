#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
ang = float(input('Digite o valor do ângulo: '))
rad = math.radians(ang)
print(f'O valor do seno é {math.sin(rad):.2f}'
      f'\nO valor do cosseno é {math.cos(rad):.2f}'
      f'\nO valor da tangente é {math.tan(rad):.2f}')