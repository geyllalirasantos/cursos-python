#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

print('CHECAGEM DE NÚMEROS PRIMOS')
num = int(input('Digite um número: '))

if num > 1:
    for i in range (2, (num+1)):
        if num % i == 0:
            print(f'O número {num} não é primo!')
            break
        else:
            print(f'O número {num} é primo')
            break

elif num == 0:
    print('O número digitado é 0')
elif num == 1:
    print('O número digitado é 1')
else:
    print('O número é negativo')