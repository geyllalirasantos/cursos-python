#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão aritmética: '))

c = 1
fst = t

while c <= 10:
    #decimo = t + (10 - 1) * r
    print(f'{t}', end=' -> ')
    t += r
    c += 1
print('FIM')