#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
#APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

texto = str(input('Digite uma frase (sem acentos): ')).strip().upper()
palavras = texto.split()
junto = ''.join(palavras)
inverso = ''

''' COMO USAR SEM FOR
inverso == junto [::-1]
'''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto:
    print('É palíndrono!')
else:
    print('Não é palíndrono.')