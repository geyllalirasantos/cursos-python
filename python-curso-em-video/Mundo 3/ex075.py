#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

valor = (int(input(f'Digite o primeiro valor: ')),
         int(input(f'Digite o segundo valor: ')),
         int(input(f'Digite o terceiro valor: ')),
         int(input(f'Digite o quarto valor: ')))

print('-' * 40)
print(f'- O numero 9 apareceu {valor.count(9)} veze(s).')
if 3 in valor:
    print(f'- O primeiro valor 3 digitado está na posição {valor.index(3)+1}')
else:
    print('- O número 3 não foi digitado nenhuma vez.')
print(f'- Os valores pares digitados foram: ', end='')
for n in valor:
    if n % 2 == 0:
        print(n, end=' ')