#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

numeros = [n1, n2, n3]
menor = min(numeros)
maior = max(numeros)

print(f'O menor valor digitafo foi {menor}\n'
      f'O maior valor digitado foi {maior}')