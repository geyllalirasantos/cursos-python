#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

turma = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    turma.append([nome, [nota1, nota2], media])

    choice = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if choice in 'N':
        break

print('-' * 40)
print(f'{"No":<8}{"NOME":<18}{"MÉDIA":>8}')
for i, l in enumerate(turma):
    print(f'{i:<4} | aluno: {l[0]:<10} | média: {l[2]:>8.1f}')
print('-' * 40)

while True:
    n = int(input('Mostrar as notas de qual aluno? [999 para finalizar]: '))
    if n == 999:
        print('FINALIZANDO...')
        break

    if n <= len(turma) -1:
        print(f'As notas de {turma[n][0]} são {turma[n][1]}')

print('PROGRAMA FINALIZADO!')

'''turma = []
dados = []

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    turma.append(dados[:])
    dados.clear()

    choice = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if choice in 'N':
        break

print('-' * 40)
print(f'{"No":<8}{"NOME":<18}{"MÉDIA":>8}')
for i, l in enumerate(turma):
    media = (l[1]+l[2])/2
    print(f'{i:<4} | aluno: {l[0]:<10} | média: {media:>8.1f}')
print('-' * 40)

while True:
    n = int(input('Mostrar as notas de qual aluno? [999 para finalizar]: '))
    if n == 999:
        print('FINALIZANDO...')
        break

    if n == i:
        print(f'As notas de {l[0]} são {l[1], l[2]}')

print('PROGRAMA FINALIZADO!')'''