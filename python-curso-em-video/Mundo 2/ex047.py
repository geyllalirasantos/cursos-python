#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=' ')
print('FIM')


'''
COMO PODERIA TER SIDO RESOLVIDO SEM MENOS LAÇOS DE REPETIÇÕES:

for n in range(2, 51, 2):
    print(n, end=' ')
print('Acabou')
'''