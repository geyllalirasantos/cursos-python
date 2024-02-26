#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão aritmética: '))

c = 1
fst = t
termos = 0
mais = 10

while mais != 0:
    termos += mais
    while c <= termos:
        print(f'{t}', end=' -> ')
        t += r
        c += 1


    print('PAUSA')
    mais = int(input('Quantos termos mais você quer mostrar? '))
print(f'Progressão finalizada com {termos} termos mostrados')