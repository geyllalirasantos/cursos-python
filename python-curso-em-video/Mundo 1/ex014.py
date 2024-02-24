#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

tc = float(input('Qual a temperatura em ºC? '))
tf = 9 * tc / 5 + 32
print(f'{tc}ºC equivale a {tf:.1f}ºF')