#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
#Calcule e mostre o comprimento da hipotenusa.

import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
#h1 = (co ** 2 + ca ** + 2) ** (1/2)
#print(f'A hipotenusa vai medir {h1:.2f}')
h1 = math.hypot(co, ca)
print(f'A hipotenusa vai medir {h1:.2f}')