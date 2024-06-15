#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte
#o programa deve ler um número pelo teclado e mostrar por extenso

lista = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
            'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
            'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um númeror entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {lista[n]}')

'''
n = int(input('Digite um número entre 0 e 20: '))
for pos, extenso in enumerate(numeros):
    if n == pos:
        print(f'Você digitou o número {extenso}.')
    elif n < 0 or n > 20:
        print('Tente novamente. Digite um número entre 0 e 20.')
        break
'''