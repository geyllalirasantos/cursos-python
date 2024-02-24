#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip()
nomes = nome.split()
print(f'O seu primeiro nome é {nomes[0]}')
print(f'O seu último nome é {nomes[len(nomes)-1]}')