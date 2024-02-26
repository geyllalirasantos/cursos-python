#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

print('-=' * 20)
print('CONVERSOR DE NÚMEROS INTEIROS')
print('-=' * 20)
n = int(input('Digite um número inteiro: '))

#lista = [1, 2, 3]
base = int(input('Escolha uma base de conversão para o seu número inteiro:\n'
      '1 - Binário\n2 - Octal\n3 - Hexadecimal\nSua opção: '))


if base == 1:
    bin = (bin(n)[2:])
    print(f'\nO número {n} em binário é: {bin}')
elif base == 2:
    oct = (oct(n)[2:])
    print(f'O número {n} em octal é: {oct}')
elif base == 3:
    hex = (hex(n)[2:])
    print(f'O número {n} em hexadecimal é: {hex}')
else:
    print('Escolha uma opção de conversão válida!')