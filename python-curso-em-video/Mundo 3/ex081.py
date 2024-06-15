#Crie um programa que vai ler vários números e colocar em uma lista.                  
# Depois disso, mostre:
# - Quantos números foram digitados.                                                                                                                    
# - A lista de valores, ordenada de forma decrescente.                                                                                          
# - Se o valor 5 foi digitado e está ou não na lista.

numeros = list()
while True:
    n = int(input('Digite um valor: '))

    if n not in numeros:
        numeros.append(n)

    choice = str(input('Quer continuar[S/N]? ')).upper().strip()[0]
    if choice in 'N':
        break


print('-' * 40)
print(f'Você digitou {len(numeros)} elementos na lista.')
numeros.sort(reverse=True)
print(f'Os valores digitados em ordem decrescente são {numeros}.')
if 5 in numeros:
    print('O número 5 faz parte da lista.')
else:
    print('O número 5 não faz parte da lista.')